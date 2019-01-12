import tensorflow as tf
import pickle
import cv2
import os
import os.path as path
from utils import predict
from model import dilation_model_pretrained
from datasets import CONFIG
import glob

if __name__ == '__main__':

    dataset = 'cityscapes'

    ## set test path
    test_path = './data/video-frames'
    test_paths = glob.glob(path.join(test_path, '*'))
    test_size = len(test_paths)


    # Create checkpoint directory
    checkpoint_dir = path.join('data/checkpoint', 'dilation_' + dataset)
    if not path.exists(checkpoint_dir):
        os.makedirs(checkpoint_dir)
    
    # Create predict image directory
    output_dir = test_path+'_output'
    if not path.exists(output_dir):
        os.makedirs(output_dir)


    with tf.Session() as sess:
        print("loading model")
        saver = tf.train.import_meta_graph(path.join(checkpoint_dir, 'dilation.meta'))
        saver.restore(sess, tf.train.latest_checkpoint(checkpoint_dir))

        graph = tf.get_default_graph()
        model = graph.get_tensor_by_name('softmax:0')
        model = tf.reshape(model, shape=(1,)+CONFIG[dataset]['output_shape'])
        input_tensor = graph.get_tensor_by_name('input_placeholder:0')

        index = 1
        for read_path in test_paths:
            input_image = cv2.imread(read_path)
            ## resize image
            input_image = cv2.resize(input_image, (2048, 1024))

            predicted_image = predict(input_image, input_tensor, model, dataset, sess)
            predicted_image = cv2.cvtColor(predicted_image, cv2.COLOR_BGR2RGB)

            output_image_path = path.join(output_dir, path.split(read_path)[1])
            cv2.imwrite(output_image_path, predicted_image)
            print("Predicting images, progress: {}/{}".format(index, test_size)+"; Saved: "+output_image_path, end='\r', flush=True)
            index += 1
        
    print("------------------------------")
    print("predict finished!")
    print("results saved in"+output_dir)

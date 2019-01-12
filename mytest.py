import tensorflow as tf
import pickle
import cv2
import os
import os.path as path
from utils import predict
from model import dilation_model_pretrained
from datasets import CONFIG

if __name__ == '__main__':

    dataset = 'cityscapes'

    ## set test path
    test_path = './data/bonn'
    test_paths = glob.glob(path.join(test_path, '*.png')

    with tf.Session() as sess:

        saver = tf.train.import_meta_graph(path.join(checkpoint_dir, 'dilation.meta'))
        saver.restore(sess, tf.train.latest_checkpoint(checkpoint_dir))

        graph = tf.get_default_graph()
        model = graph.get_tensor_by_name('softmax:0')
        model = tf.reshape(model, shape=(1,)+CONFIG[dataset]['output_shape'])
        input_tensor = graph.get_tensor_by_name('input_placeholder:0')

        for read_path in test_paths:
            input_image = cv2.imread(read_path)
            predicted_image = predict(input_image, input_tensor, model, dataset, sess)
            predicted_image = cv2.cvtColor(predicted_image, cv2.COLOR_BGR2RGB)

            output_image_path = path.joint(read_path.split(".png")[0], "_predict.png")
            cv2.imwrite(output_image_path, predicted_image)

import cv2
import os
import os.path as path
from utils import predict
from model import dilation_model_pretrained
from datasets import CONFIG
import glob

if __name__ == '__main__':
    image_folder = './data/video_frames/'
    video_name = 'video.avi'

    # images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]
    # frame = cv2.imread(os.path.join(image_folder, images[0]))
    # height, width, layers = frame.shape

    # video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    # for image in images:
    #     video.write(cv2.imread(os.path.join(image_folder, image)))

    # cv2.destroyAllWindows()
    # video.release()

    paths = os.listdir(image_folder)
    print(paths)
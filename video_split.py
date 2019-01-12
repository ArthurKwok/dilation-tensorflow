import tensorflow as tf
import pickle
import cv2
import os
import os.path as path
from utils import predict
from model import dilation_model_pretrained
from datasets import CONFIG
import glob
import numpy as np

if __name__ == '__main__':

    video_path = './data/test_video.mp4'
    frame_path = './data/video_frames/'

    frame_num = 1
    clip = cv2.VideoCapture(video_path)
    if clip.isOpened():
        rval, frame = clip.read()
    else:
        rval = False
    while rval:
        rval, frame = clip.read()
        cv2.imwrite(path.join(frame_path, "frame{:0>5d}.png".format(frame_num)))


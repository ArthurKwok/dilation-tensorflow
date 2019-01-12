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
    frame_dir = './data/video_frames/'
    if not path.exists(frame_dir):
        os.makedirs(frame_dir)

    frame_num = 1
    clip = cv2.VideoCapture(video_path)
    if clip.isOpened():
        print("read video")
        rval, frame = clip.read()
    else:
        rval = False
    while rval:
        rval, frame = clip.read()
        print("Saving frame {:0>5d}".format(frame_num), end='\r', flush=True)
        cv2.imwrite(path.join(frame_path, "frame{:0>5d}.png".format(frame_num)))


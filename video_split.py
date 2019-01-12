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
from moviepy.editor import VideoFileClip

if __name__ == '__main__':

    video_path = 'videoplayback_clip.mp4'
    frame_dir = './data/video_frames/'
    if not path.exists(frame_dir):
        os.makedirs(frame_dir)

    frame_num = 1
    clip = VideoFileClip(video_path)
    "Reading video.."
    for frames in clip.iter_frames():
        cv2.imwrite(path.join(frame_dir, "frame{:0>5d}.png".format(frame_num)), frames)
        print("Saving frame: {:0>5d}".format(frame_num), end='\r', flush=True)
        frame_num +=1
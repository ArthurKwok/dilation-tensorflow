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

    dataset = 'cityscapes'

    test_path1 = './data/bonn'
    test_paths1 = glob.glob(path.join(test_path1, '*.png'))

    test_path2 = './data/video-frames'
    test_paths2 = glob.glob(path.join(test_path2, '*.jpg'))

    image1 = cv2.imread(test_paths1[0])
    image2 = cv2.imread(test_paths2[0])
    image2 = cv2.resize(image2, (2048,1024))

    print(image1.shape)
    print(image1.dtype)
    print(image2.shape)
    print(image2.dtype)

import cv2
import os
import os.path as path
from utils import predict
from model import dilation_model_pretrained
from datasets import CONFIG
import glob

if __name__ == '__main__':
    pathIn = './data/video_frames/'
    pathOut = 'video.avi'
    fps = 30

    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))

    print(files)
    # for i in range(len(files)):
    #     filename=pathIn + files[i]
    #     #reading each files
    #     img = cv2.imread(filename)
    #     height, width, layers = img.shape
    #     size = (width,height)
    #     print(filename)
    #     #inserting the frames into an image array
    #     frame_array.append(img)
 
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    # for i in range(len(frame_array)):
    #     # writing to a image array
    #     out.write(frame_array[i])
    # out.release()
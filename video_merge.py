import cv2
import numpy as np
import os

if __name__ == '__main__':
    pathIn = './data/video_frames/'

    os.system("cd "+ os.path.split(pathIn))
    print(os.system("ffmpeg -framerate 30 -i frame%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4"))

    # frame_array = []
    # files = [f for f in os.listdir(pathIn) if os.path.isfile(os.path.join(pathIn, f))]
 
    # #for sorting the file names properly
    # files.sort(key = lambda x: int(x[5:-4]))

    # for i in range(len(files)):
    #     filename = pathIn + files[i]
    #     #reading each files
    #     img = cv2.imread(filename)
    #     height, width, layers = img.shape
    #     size = (width,height)
    #     print("Reading... {}/{}".format(i, len(files)), end='\r', flush=True)
    #     #inserting the frames into an image array
    #     frame_array.append(img)

 
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    # for i in range(len(frame_array)):
    #     # writing to a image array
    #     out.write(frame_array[i])
    #     print("Merging... {}/{}".format(i, len(frame_array)), end='\r', flush=True)
    # out.release()
    # print("Video saved as: "+pathOut)
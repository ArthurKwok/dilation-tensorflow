import cv2
import os
from tqdm import tqdm
import glob

if __name__ == '__main__':

    """"""
    image_folder = './data/video_frames_output/*'
    video_name = 'video.avi'#save as .avi
    #is changeable but maintain same h&w over all  frames
    width = 2048
    height = 1024 
    #this fourcc best compatible for avi
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    video=cv2.VideoWriter(video_name,fourcc, 2.0, (width,height))

    for i in tqdm((sorted(glob.glob(image_folder),key=os.path.getmtime))):
        x=cv2.imread(i)
        video.write(x)

    cv2.destroyAllWindows()
    video.release()


    """"""
    # os.system("cd "+ os.path.split(pathIn)[0])
    # print(os.system("ffmpeg -framerate 30 -i frame%05d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4"))

    """"""
    # pathIn = './data/video_frames/'
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
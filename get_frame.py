import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_name", help="name of video file")
parser.add_argument("-n", "--num_of_img", type=int, help="number of image you want to get")
parser.add_argument("-r", "--rotate_angle", choices=["-90", "0", "90"], default="0", help="angle to rotate image: -90/0/90")
args = vars(parser.parse_args())
print(args)

file_name = args['file_name']
num_img_out = args['num_of_img']-1
out_folder = 'img_out'

rot = 0
if args['rotate_angle'] == "90":
    rot = cv2.ROTATE_90_CLOCKWISE
elif args['rotate_angle'] == "-90":
    rot = cv2.ROTATE_90_COUNTERCLOCKWISE

videoCaptureObject = cv2.VideoCapture(file_name)
frame_count = int(videoCaptureObject.get(cv2. CAP_PROP_FRAME_COUNT))
jump = int(frame_count/num_img_out)

if not os.path.isdir(out_folder):
    os.makedirs(out_folder)
count = 0
img_count = 0
while(count < frame_count):
    ret,frame = videoCaptureObject.read()
    if count % jump == 0:
        if rot != 0:
            frame = cv2.rotate(frame, rot)
        cv2.imwrite(out_folder+"/"+file_name[:-3]+"{:d}.jpg".format(img_count+1), frame)
        img_count += 1
    count += 1
videoCaptureObject.release()

import os

img_dir = "images"
index = 10113
max_file_idx = 299 # max idx name of img file
file_prefix = '/20221014_074954.' # prefix of img file capturing from video

for i in range(1,max_file_idx):
    fn = img_dir+file_prefix+str(i)+'.jpg'
    if os.path.exists(fn):
        os.rename(fn, img_dir+'/'+ str(index).zfill(8)+'.jpg')
        index += 1


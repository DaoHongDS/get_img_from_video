import cv2
import time
import os

img_folder = '/images/'
video_file = 'test.mp4'
try:
  os.mkdir(img_folder)
except OSError:
  pass

# Log the time
time_start = time.time()

# Start capturing the feed
cap = cv2.VideoCapture(video_file)

# Find the number of frames
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print ("Number of frames: ", video_length)
count = 0
print ("Converting video..\n")

# Start converting the video
while cap.isOpened():
  # Extract the frame
  ret, frame = cap.read()
  if not ret:
    continue

  # Write the results back to output location.
  cv2.imwrite(img_folder + "/%#05d.jpg" % (count+1), frame)
  count = count + 1

  # If there are no more frames left
  if (count > (video_length-1)):
    # Log the time again
    time_end = time.time()

    # Release the feed
    cap.release()
    # Print stats
    print ("Done extracting frames.\n%d frames extracted" % count)
    print ("It took %d seconds forconversion." % (time_end-time_start))
    break
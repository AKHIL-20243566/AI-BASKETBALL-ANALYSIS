import cv2
import os

def read_video(video_path):
    cap=cv2.VideoCapture(video_path) # captures the video from the file path 
    frames =[] #Store the frame coordinates in a list 
    while True: # Looping over each frame and storing the needed frame
        ret,frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames # return the list of frames

def save_video(output_video_frames, output_video_path):
    if not os.path.exists(os.path.dirname(output_video_path)): #if directory name exists then no need of this , if not then create the directory
        os.makedirs(os.path.dirname(output_video_path))
    fourcc = cv2.VideoWriter_fourcc(*"XVID") #save the video in XVID format
    out=cv2.VideoWriter(output_video_path, fourcc, 24.0, (output_video_frames[0].shape[1], output_video_frames[0].shape[0])) # 24.0 is the fps and shape[1] is width and shape[0] is height
    for frame in output_video_frames:
        out.write(frame) # writing each frame to the output video
    out.release() # releasing the video writer object

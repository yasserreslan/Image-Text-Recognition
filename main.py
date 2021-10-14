import pytesseract
import cv2
import numpy as np
from pytube import YouTube

from enhance import enhance

import os




#Ensure video does not download every time we run
if (os.path.isfile("textvid.mp4")):
  pass

#Download video for the first time for usage
else:
  print("Downloading video from Youtube...")
  yt = YouTube('https://www.youtube.com/watch?v=9Nt9b2OKv9Y')

  ys = yt.streams.filter(res="480p").first().download(filename="textvid.mp4")






# #initliaze our video path
video = cv2.VideoCapture("textvid.mp4")



# while vid.isOpened():
#   ret,frame = vid.read()
#   frame = frame[222:250,415:]
#   cv2.imwrite("newtube.png",frame)
  
#   break


prev_txt = None

while video.isOpened():
    ret,frame = video.read()

    if not ret:
        break

    #Preprocessing image using cv2 (enhance.py file)
    gray = enhance(frame[222:250,415:750])

    #Pytesseract custom configuration based on image input
    custom_config = '--psm 7 --oem 3 '
    
    #Show Desired frame with preprocessing applied
    cv2.imshow("img",gray)

    #Using Google's OCR text detector model with custom configuration
    txt = pytesseract.image_to_string(gray, config=custom_config,lang='eng')


    #Only show detected text
    if prev_txt != txt:
      print(txt)

    prev_txt = txt


    #create a OpenCv rectangle around the desired frame
    start_pt = (415,250)
    end_pt= (750,222)
    color = (0,0,255)
    thickness = 2

    frame = cv2.rectangle(frame,start_pt, end_pt, color, thickness)



    #Show the video
    cv2.imshow("fr",frame)

    #to stop the video processing manually
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break




video.release()
cv2.destroyAllWindows()
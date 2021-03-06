import cv2
import math

import os, os.path
mypath = "/var/www/html/videoverification/images"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))
videoFile = "uploads/sample.mp4"
imagesFolder = "images/"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
i=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read() #reads the video whether any frames is there if any returns ret=true
    if (ret != True):
        break
    filename = imagesFolder + "image" +  str(i) + ".jpg"
    cv2.imwrite(filename, frame)
    i=i+1
cap.release()

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['videoverification']
coll = db['videoKeys']

count=0

for root, dirs, files in os.walk(mypath):
    for file in files:
        count=count+1		

coll.delete_many({})
print(count)
coll.insert({"countBlock":1,"count":count-1})




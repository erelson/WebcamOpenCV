#! /usr/bin/env python

"""
Adapted from:
http://stackoverflow.com/questions/2601194/displaying-webcam-feed-using-opencv-and-python 
"""

import cv2.cv as cv

#cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("w1", cv.CV_WINDOW_NORMAL)
cv.ResizeWindow("w1", 900,650)
#capture = cv.CaptureFromCAM(0)
for i in range(10):
    capture = cv.CaptureFromCAM(i)
    if capture: break
print i

def repeat():

    global capture #declare as globals since we are assigning to them now
    global camera_index
    frame = cv.QueryFrame(capture)
    cv.ShowImage("w1", frame)
    c = cv.WaitKey(10)


while True:
    repeat()


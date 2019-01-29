import sys
import re
import os
import numpy as np
import cv2
import pickle

def main():
    dataDict = load_obj('track1_road.pkl')
    entryPt = dataDict['c010']['en']
    exitPt = dataDict['c010']['ex']
    
    en1, en2, en3, en4 = [], [], [], []
    ex1, ex2, ex3, ex4 = [], [], [], []
    
    for point in entryPt:
        if (point[0] < 250):
            en1.append(point)
        elif (point[0] > 1300):
            en3.append(point)
        elif (point[1] < 200):
            en2.append(point)
        else:
            en4.append(point)
            
    for point in exitPt:
        if (point[0] < 250):
            ex1.append(point)
        elif (point[0] > 1300):
            ex3.append(point)
        elif (point[1] < 200):
            en2.append(point)
        else:
            en4.append(point)


    side1 = {'en': en1, 'ex': ex1}
    side2 = {'en': en2, 'ex': ex2}
    side3 = {'en': en3, 'ex': ex3}
    side4 = {'en': en4, 'ex': ex4}
    
    print("side3: ")
    print(side3)
    
    cap = cv2.VideoCapture('../../train/s03/c010/vdo.avi')
    
    ret, frame = cap.read()
    if not ret:
        exit(0)
        
    for entries in entryPt:
        entries = tuple(map(int,entries))
        cv2.circle(frame, entries, 10, (0,0,255), -1)
    for exits in exitPt:
        exits = tuple(map(int,exits))
        cv2.circle(frame, exits, 10, (255,0,0), -1)
    
#    mid1 = ()
#    difX1, difY1 = 0, 0
#    mid2 = ()
#    difX2, difY2 = 0, 0
#    mid3 = ()
#    difX3, difY3 = 0, 0
#    mid4 = ()
#    difX4, difY4 = 0, 0
#    for point in side1:
#        mid1 = 
    
    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('../../train/s03/c010/vdo.avi', frame)    
    cv2.waitKey(0)
    
        
# Load an object from the file system
def load_obj(name):
    f = open(name, 'rb')   # 'r' for reading 
    mydict = pickle.load(f)       
    f.close()                       

    return mydict;

if __name__ == "__main__":
    main()
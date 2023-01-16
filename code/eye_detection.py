import array as arr
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

import cv2

root = os.getcwd()
print(root)


eye_cascade = cv2.CascadeClassifier(root +"\\eye_self_train.xml")
cap = cv2.VideoCapture(root + '\\video\\zp65_facecam.mp4')
i = 0
j = 0
arry = []
arry1 = []
while cap.isOpened():
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray, (1, 1), 2)
    faces = eye_cascade.detectMultiScale(gaussian_blur,1.1,4)
    for (x, y , w , h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,0),2)
        i = i +0.092
        if (x-348<20):
            z = x - 346
            arry.insert(j,z)
            arry1.insert(j,i)
            j = j + 1
            # naming the x axis 
            plt.xlabel('Time(sec)') 
            # naming the y axis 
            plt.ylabel('Eye Motion(Left,right)') 
  
            # giving a title to my graph 
            plt.title('Eye Motion')
            if(i>=90):
                # Plot the data
                plt.plot(arry1, arry, label='Eye_tracking')
                plt.xlabel('Time(sec)') 
                # naming the y axis 
                plt.ylabel('Eye Motion(Left,right)') 
  
                # giving a title to my graph 
                plt.title('Eye Motion')

                # Add a legend
                plt.legend()

                # Show the plot
                plt.show()
    #Display the output
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print(i)
        print('Updated List: ', arry)
        print(len(arry))
        break
cap.release()
cap.distroyAllWindows()
                       

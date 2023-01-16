import array as arr
import numpy as np
import matplotlib.pyplot as plt
import cv2

eye_cascade = cv2.CascadeClassifier('eye_self_train.xml')
input_video = cv2.VideoCapture('fmri_p1.mp4')

timestamp_axis = []
left_right_movement = []
up_down_movement = []
eye_blinking = []
frame_number = 1
previous_frame = None
timestamp_axis_array_index = 0
left_right_arry_index = 0
up_down_arry_index = 0
eye_blinking_arry_index = 0
previous_z_value = 0
previous_q_value = 0
#initial point of left_right_movement 
x = 348
#initial point of up_down_movement
y = 275
while input_video.isOpened():
    _,img = input_video.read()
    #obtain current frame time
    current_frame_time = int(input_video.get(cv2.CAP_PROP_POS_MSEC))
    #insert current frame time value in timestamp_axis array
    timestamp_axis.insert(timestamp_axis_array_index,current_frame_time)
    #increment in timestamp_axis arry index
    timestamp_axis_array_index = timestamp_axis_array_index + 1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray, (1, 1), 2)
    eyes = eye_cascade.detectMultiScale(gaussian_blur,1.1,4)
    #initially set right_left_movement point as zero position 
    z = x - 348
    #if x value not change that's mean we obtain previous value of x that
    #indicates eye is blinking
    if z == 0:
        #if eye is blinking we obtain 1 value
        eye_blinking.insert(eye_blinking_arry_index , 1)
        eye_blinking_arry_index = eye_blinking_arry_index +1
    else:
        #if eye is not blinking we obtain 0 value
        eye_blinking.insert(eye_blinking_arry_index , 0)
        eye_blinking_arry_index = eye_blinking_arry_index +1
    #Those values of x that are obtain due to worng detection is removed by
    # apply if(z>20) condition
    if(z > 20):
        z = 0
    #if previous value of x is not equal to new value of x then insert new value in array otherwise insert 0(not change in value indicates eye is blinking)
    if not previous_z_value == z:
        left_right_movement.insert(left_right_arry_index,z)
        previous_z_value = z
        left_right_arry_index = left_right_arry_index +1
    else:
        left_right_movement.insert(left_right_arry_index,0)
        previous_z_value = z
        left_right_arry_index = left_right_arry_index+1
    print("Length of x_arry: ",len(left_right_movement))
    #initially set up_right_movement point as zero position
    q = y - 275
    #Those values of y that are obtain due to worng detection is removed by
    # apply if(y<-20) condition
    if(q < -20):
        q = 0
    #if previous value of y is not equal to new value of y then insert new value in array otherwise insert 0(not change in value indicates eye is blinking)
    if not previous_q_value == q:
        up_down_movement.insert(up_down_arry_index ,q)
        previous_q_value = q
        up_down_arry_index = up_down_arry_index +1
    else:
        up_down_movement.insert(up_down_arry_index,0)
        previous_q_value = q
        up_down_arry_index = up_down_arry_index +1
  #  print("Length of y_arry: ",len(up_down_movement))

    for (x, y , w , h) in eyes:
        cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,0),2)
        if (len(timestamp_axis) == 2237): #2237 is the total timestamp of video (each fram is  40msec)
            plt.plot(timestamp_axis, left_right_movement, 'g-', label='left_right_movement')
            plt.plot(timestamp_axis, up_down_movement, 'r-', label='up_down_movement')
            plt.plot(timestamp_axis, eye_blinking , 'b-', label='Eye_blinking')
            plt.legend(loc='best')
            plt.xlabel('Time(msec)') 
            # naming the y axis 
            plt.ylabel('Eye Motion') 
            # giving a title to my graph 
            plt.title('Eye Motion Tracking')
            # Show the plot
            plt.show()
        
    #Display the output
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cap.distroyAllWindows()

import cv2
import os
import sys


def detect_eye(test_image, ):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    # convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    return image_copy


def main():
    # Assigning our previous_frame to None
    previous_frame = None
    root = os.getcwd()
    cap = cv2.VideoCapture(root + '\\video\\zp65_facecam.mp4')
    if cap is None:
        print('Failed to load video:')
        sys.exit(1)
    frame_number = 1
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    timestamps_x_axis = []
    duration = (total_frames / fps) * 1000  # in ms
    print("total_frames:{0}, width:{1}, Height:{2}, FPS:{3}, duration:{4}".format(total_frames, width, height, fps,
                                                                                  duration))

    while cap.isOpened():
        is_frame_exists, current_frame = cap.read()
        if is_frame_exists:
            motion = 0

            # Converting color image to gray_scale image
            gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

            # Converting gray_frame scale image to GaussianBlur
            # so that change can be find easily
            gaussian_blur = cv2.GaussianBlur(gray_frame, (1, 1), 0)

            # In first iteration we assign the value
            # of previous_frame to our first current_frame
            if previous_frame is None:
                previous_frame = gaussian_blur
                continue
            # Difference between static background
            # and current current_frame(which is GaussianBlur)
            diff_frame = cv2.absdiff(previous_frame, gray_frame)

            # If change in between static background and
            # current current_frame is greater than 30 it will show white color(255)
            thresh_frame = cv2.threshold(diff_frame, 60, 255, cv2.THRESH_BINARY)[1]
            dilated = cv2.dilate(thresh_frame, None, iterations=1)

            c, h = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            cv2.drawContours(previous_frame, c, -1, (0, 255, 0), 2)
            # if frame_number < 201: # simple check to only save 200 frames for training
            #    cv2.imwrite(root + '\\images\\img_'+ str(frame_number) + '.jpg',previous_frame)
            cv2.imshow("Eye Motion Detection", previous_frame)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            previous_frame = gray_frame
            frame_number = frame_number + 1

        else:
            break
    cap.release()
    cv2.destroyAllWindows()


main()
print('Program Finished')

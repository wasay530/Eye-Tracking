# Dataset Description

We conducted a short fMRI session, but without the actual fMRI running. Instead, we only setup the face videocamera and the good eye-tracker. The session started with three fake calibration screens to provide a ground truth of where I am looking on various points on the screen. Afterwards, we ran a shortened "normal" session with five comprehension tasks, two control tasks, and seven distractor and rest phases.


 #   Dataset Upload
 
I uploaded all data here: https://cloud.lin-magdeburg.de/s/WQi96tMSAE57MSH
  
  
# Dataset Hints & Notes


I strongly suggest to watch the zp65_facecam_screen.mp4 file first. I put the facecam, stimuli, and eye-tracker data together and synced it. You can watch this in double speed or so, but should give you a good idea of the gathered data. The video is not perfect in terms of synchronization (it is sometimes off a few hundred milliseconds, but it should be fine for informative purposes) and eye-tracker visualization.



The actual facecam video is "zp65_facecam.mp4". Note that the video starts around 17 seconds before the session and stimuli start. So you could cut that first part, if you want to align stimuli to your x/y coordinate extraction. Since I was in the scanner, I couldn't supervise the camera setup. My colleagues put it much closer to the eye than last time, which in this case may even be helpful? Let me know if you need a video further zoomed out.



The two "zp65_*.csv" files contain which stimuli was shown at what time and where the eye-tracker located my eyes (GazePosX/GazePosY), including pupil dilation. The gaze position coordinates assume that (0,0) is the top-left of the screen. The "_preprocessed.csv" is in the original temporal resolution of the eye-tracker (500 Hertz). For your convenience, I also provided a downsampled version "_downsampled.csv" with a lower temporal resolution that aligns with the facecam video at 25 Hertz. In both versions, the first line in the csv file is already ~17 seconds after the video starts. In the next session, I'll try to figure out how to exactly align the video and stimuli.



In the "/stimuli" folder, you can find the presented stimuli as images if you want to overlay your extracted eye-tracking maps.



Unfortunately, the face videocamera didn't save a file when we first tried to do this. Thus, the data I provided is from a second session. You may be able to tell from my eye gaze that I had already looked at the same snippets half an hour beforehand. But I tried to simulate a normal reading behavior.

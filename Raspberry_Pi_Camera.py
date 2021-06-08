import picamera
import time

camera = picamera.PiCamera()

"""
To take a picture and give it a name:
camera.capture("pict.jpg")

To PREVIEW video on Raspberry Pi camera:
camera.start_preview()
camera.stop_preview()

To RECORD a video:
camera.start_recording("vid.h264")
time.sleep(10)
camera.stop_recording()

To do a timelapse photography
camera.capture_continuous("filename")
"""

print("Program finished")

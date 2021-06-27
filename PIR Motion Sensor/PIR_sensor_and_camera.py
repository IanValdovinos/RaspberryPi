"""
This program attempts to use the PIR motion sensor and trigger a camera shot when the sensor
detects any movement.

Helpful resources:
https://projects.raspberrypi.org/en/projects/parent-detector/3
"""

from gpiozero import MotionSensor
import time
from picamera import PiCamera

print("Starting script")

pir = MotionSensor(14)
camera = PiCamera()

filename = "intruder.h264"
recording = False

while True:
  if (pir.motion_detected):
    print("Motion detected! Recording bitch.")
    camera.start_recording(filename)
    recording = True
    time.sleep(10)
    camera.stop_recording()

  time.sleep(1)

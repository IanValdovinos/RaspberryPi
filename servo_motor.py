"""
This program will test the GPIO pins with a servor motor through PWM
"""
print("Program begins")

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32, GPIO.OUT)
print("Board and pins are set up")

pwm = GPIO.PWM(32, 50)
pwm.start(0)
print("PWM pin is ready to go")

for i in range(10):
    print("Moving servo to the RIGHT")
    pwm.ChangeDutyCycle(i)
    time.sleep(0.5)

for i in range(10, 0, -1):
    print("Moving servo to the LEFT")
    pwm.ChangeDutyCycle(i)
    time.sleep(0.5)

print("Pogram finished")

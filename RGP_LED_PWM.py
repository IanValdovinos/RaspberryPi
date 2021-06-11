"""
This Program controls an RGB LED through PWM
Ian Samuel Valdovinos Granados
"""

import RPi.GPIO as GPIO
import time

led_1_pin = 32


# Set pin and board modes
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led_1_pin, GPIO.OUT)

# Setup LED pins as PWM output pins 
pwm_1 = GPIO.PWM(led_1_pin, 50)
pwm_1.start(0)


while True:
    for i in range(0, 50):
        pwm_1.ChangeDutyCycle(i)
        time.sleep(0.1)

    for i in range(50, 0, -1):
        pwm_1.ChangeDutyCycle(i)
        time.sleep(0.1)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led = 8
GPIO.setup(led,GPIO.OUT)

user_in_str = input("How many times do you want the led to blink? ")
user_in_int = int(user_in_str)

for i in range(user_in_int):
    GPIO.output(led, True)
    time.sleep(0.2)
    GPIO.output(led, False)
    time.sleep(0.2)

print("Done!")
    


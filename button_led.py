import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led_pin= 8
GPIO.setup(led_pin, GPIO.OUT)

button_pin = 10
GPIO.setup(button_pin, GPIO.IN)

while True:
  
  GPIO.output(led_pin, True)
  time.sleep(0.3)
  GPIO.output(led_pin, False)
  time.sleep(0.3)

  button_status = GPIO.input(button_pin)
  print("Button status:", button_status)

  while button_status:
    GPIO.output(led_pin, True)
    button_status = GPIO.input(button_pin)






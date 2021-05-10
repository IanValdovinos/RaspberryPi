import RPi.GPIO as GPIO

print("Import successful")

"""
Select pin numbering mode:
GPIO.setmode(GPIO.BOARD)
or
GPIO.setmode(GPIO.BCM)
"""
GPIO.setmode(GPIO.BOARD)

"""
Setup a pin for input or output:
GPIO.setup(13, GPIO.OUT)
GPIO.setup(13, GPIO.IN)
"""

"""
Assign a value to an outpin pin:
GPIO.output(13, True)
"""

"""
Reading input pins:
value = GPIO.input(13)
"""

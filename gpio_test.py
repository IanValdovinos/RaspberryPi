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

"""
PWM
pwm_obj = GPIO.PWM(18, 400)  #Second argument is the frequency
pwm_obj.start(100) # Argument is the duty cycle (percentage)
pwm_obj.ChangeDutyCycle(50)
"""

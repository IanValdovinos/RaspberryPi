"""
This program is aimed to test Twilio to send a Whatsapp message
to a phone number when a sensor/button is activated

- Ian Valdovinos
"""

from twilio.rest import Client
import RPi.GPIO as GPIO
import time

# GPIO setup for sensor pin
GPIO.setmode(GPIO.BOARD)
sensor_pin = 12
GPIO.setup(sensor_pin, GPIO.IN)

# Twilio credentials used to gain access to Twilio services 
account_sid = ""
auth_token = ""

# Client setup
client = Client(account_sid, auth_token)

while True:
    # Get sensor/button status
    sensor_status = GPIO.input(sensor_pin)
    print(sensor_status)
    
    if sensor_status:
        # If the sensor is activated, send a message to the given phone number
        message = client.messages.create(body="Sensor activated!", from_="whatsapp:+14155238886", to="whatsapp:+12483210037")

        
    time.sleep(5)
    

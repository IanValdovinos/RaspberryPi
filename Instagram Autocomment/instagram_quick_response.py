"""
Thi program will attempt to make the first comment on a parson's post as soon
as it is posted

References:
https://github.com/ping/instagram_private_api
https://instagram-private-api.readthedocs.io/en/latest/

Useful methods:
user_feed()
username_info()
post_comment()

"""

from instagram_private_api import Client
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
listening_led = 10
GPIO.setup(listening_led, GPIO.OUT)
done_led = 8
GPIO.setup(done_led, GPIO.OUT)
GPIO.output(listening_led, False)
GPIO.output(done_led, False)

def blink_listening_led():
    for i in range(6):
        GPIO.output(listening_led, True)
        time.sleep(1)
        GPIO.output(listening_led, False)
        time.sleep(1)


my_username = "valdovinos.samuel"
my_password = "Sam132435!"
profile_to_track_username = 'd.j.valdovinos'
comment = "Nice!!"

instagram = Client(username=my_username, password=my_password)
user_info = instagram.username_info(profile_to_track_username)
user_pk = user_info['user']['pk']
user_feed = instagram.user_feed(user_pk, count=1)
last_post_pk = user_feed['items'][0]['pk']


new_post_id = last_post_pk
while new_post_id == last_post_pk:
    print('No new post.')
    user_feed = instagram.user_feed(user_pk, count=1)
    new_post_id = user_feed['items'][0]['pk']
    blink_listening_led()

print("There's a new post!")
print("Posting comment...")
instagram.post_comment(new_post_id, comment)
GPIO.output(done_led, True)
print('Done!')

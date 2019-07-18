import requests
from gpiozero import Button
from signal import pause

button = Button(2)

def send_message():
        r = requests.post(
          'https://slack.com/api/chat.postMessage',
          data = {"token": "xoxp-356823449492-675957353746-697683336935-309852e74ac7b2d58cdf0e1b38fb36ef", "channel": "CLFAYHN8L", "text": "Hi! I'm new here.", "as_user": "true", }
        )
        if (r.status_code == 200):
            print (r.content)
        else:
            print ("Oops, something went wrong.")
            print (r.content)

#send_message()

button.when_pressed = send_message
#button.when_released = 

pause()

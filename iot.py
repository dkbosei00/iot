import requests
from gpiozero import Button
from signal import pause

button = Button(2)

def send_message():
	r = requests.post(
'https://maker.ifttt.com/trigger/button_pressed/with/key/bA3F2bo0WKQHYaLGFEG6xo',
data = { "value1": "This notification", "value2": "from a python code", "value3": "my phone."}
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

# Based on Dataquest 'Working with APIs' exercise

import requests
import json

# Boston, MA latitude and longitude
parameters = {"lat": 42.36, "lon": -71.06}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

content_type = response.headers['content-type']

json_data = response.json()
first_pass_duration = json_data['response'][0]['duration']/60

response = requests.get("http://api.open-notify.org/astros.json")
json_data = response.json()
craft = json_data['people'][0]['craft']
in_space_count = json_data['number']

message = "The {} is passing Boston in {} minutes. There are {} people in space above Boston right now.".format(craft, first_pass_duration, in_space_count)

print(message)

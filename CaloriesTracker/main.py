# import requests
# import json
# import datetime as dt
#
# API_KEY = 'b26d7cba14296c65e2cd3df6194500f5'
# API_ID = '6f647819'
#
#
# url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# headers = {
#     'Content-Type': 'application/json',
#     'x-app-id': API_ID,  # Replace with your actual app id
#     'x-app-key': API_KEY  # Replace with your actual app key
# }
#
# query = input("Tell me which exercise you did: ")
# data = {
#     "query": query
# }
#
# sheety_url = 'https://api.sheety.co/af34258e0332985bea4fd0c8c39b8687/myWorkouts/workouts'
#
#
#
#
# response = requests.post(url, headers=headers, data=json.dumps(data))
#
# exercises = response.json()['exercises']
#
# present_datetime = str(dt.datetime.now()).split(' ')
#
# date = present_datetime[0]
# time = present_datetime[1]
#
#
# for exercise in exercises:
#     body = {
#         "workout": {
#             'Date': date,
#             'Time': time,
#             'Exercise': exercise['name'].title(),
#             'Duration': exercise['duration_min'],
#             'Calories': exercise['nf_calories']
#         }
#     }
#
#     print("Sheety request body:", body)
#     sheety_response = requests.post(url=sheety_url, headers={'Content-Type': 'application/json'}, data=json.dumps(body))
#     print("Sheety API response:", sheety_response.json())
#     if sheety_response.status_code != 200:
#         print("Failed to add data to Sheety:", sheety_response.json())

import requests
import json
import datetime as dt

API_KEY = 'b26d7cba14296c65e2cd3df6194500f5'
API_ID = '6f647819'

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'Content-Type': 'application/json',
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}

query = input("Tell me which exercise you did: ")
data = {
    "query": query
}

sheety_url = 'https://api.sheety.co/af34258e0332985bea4fd0c8c39b8687/myWorkouts/workouts'

# Send request to Nutritionix API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response from Nutritionix
print("Nutritionix API response status code:", response.status_code)
print("Nutritionix API response:", response.json())

if response.status_code == 200:
    exercises = response.json()['exercises']

    present_datetime = str(dt.datetime.now()).split(' ')
    date = present_datetime[0]
    time = present_datetime[1]

    for exercise in exercises:
        body = {
            "workout": {
                'Date': date,
                'Time': time,
                'Exercise': exercise['name'].title(),
                'Duration': exercise['duration_min'],
                'Calories': exercise['nf_calories']
            }
        }

        # Print the body being sent to Sheety for verification
        print("Sheety request body:", body)

        # Send request to Sheety API
        sheety_response = requests.post(url=sheety_url, headers={'Content-Type': 'application/json'},
                                        data=json.dumps(body))

        # Print the response from Sheety
        print("Sheety API response status code:", sheety_response.status_code)
        print("Sheety API response:", sheety_response.json())

        if sheety_response.status_code != 200:
            print("Failed to add data to Sheety:", sheety_response.json())
else:
    print("Failed to retrieve exercises from Nutritionix:", response.json())


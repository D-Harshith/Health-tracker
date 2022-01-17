import requests
from datetime import datetime

NUTRINIX_API_KEY = "3773cf0a77c4a135db165548a94efcc0"
NUTRINIX_API_ID = "98639c52"
NUTRINIX_API = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_API = "https://api.sheety.co/03782136f21506b06fe88d120743c87e/myWorkoutTracker/workouts"

header1 = {
    "x-app-id": NUTRINIX_API_ID,
    "x-app-key": NUTRINIX_API_KEY
}

nutri_params = {
    "query": input("What u have done? "),
    "gender": "male",
    "weight_kg": 71.5,
    "height_cm": 168,
    "age": 19
}

nutrinix_response = requests.post(url=NUTRINIX_API, json=nutri_params, headers=header1)
result = nutrinix_response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")
# print(result["exercises"][0]['duration_min'])
# today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_API, json=sheet_inputs)
#     print(sheet_response.text)
# print(result)
print("Updated!!")

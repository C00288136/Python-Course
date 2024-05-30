import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "182.88"
AGE = "22"


API_KEY = "76b9db66702d917bac0271229982ef99"
APP_ID = "0eeb2d05"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_params = {
    "query" : input("Tell me what exercise did you do ? : "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRI_ENDPOINT,json=nutri_params,headers=headers)

data = response.json()

print(data)



print(exercise_type)

SHEETY_ENDPOINT = "https://api.sheety.co/cb8eb9e122d16917dde918fcd63ff04e/myWorkouts/workouts"

today = datetime.now().strftime("%x")
time_now = datetime.now().strftime("%X")

print(today)




for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheets_response = requests.post(url=SHEETY_ENDPOINT,json=sheet_inputs)

print(sheets_response.text)
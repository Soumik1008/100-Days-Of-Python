import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('Day-38(Workout Tracking using Google Sheets)/.env')
load_dotenv(dotenv_path=dotenv_path)

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = os.environ["APP_ID"]
NUTRITIONIX_APP_KEY = os.environ["API_KEY"]
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
    "Content-Type": "application/json",
}

nutritionix_data = {
    "query": input("What exercises did you do? :"),
    "gender": "male",
    "weight_kg": 79,
    "height_cm": 176,
    "age": 22,
}

response = requests.post(NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_data)
response.raise_for_status()
result=response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
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

    #Bearer Token Authentication
    

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(
      "soumik", 
      "buntyanshi@1008"
  ))
    print(sheet_response.text)
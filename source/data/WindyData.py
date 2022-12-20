
import os
import requests
from dotenv import load_dotenv
import json
import datetime

# FOR TESTING PURPOSES ONLY

def getWindSpeed():
    # Declaring variables
    load_dotenv()
    data = {"lat": 61.55,
            "lon": 29.50,
            "model": "gfs",
            "parameters": ["wind"],
            "levels": ["surface"],
            "key": os.getenv("WINDY_API_KEY")
            }
    header = {"Content-Type": "application/json"}


    try:
        json_string = requests.post("https://api.windy.com/api/point-forecast/v2", json=data, headers=header)
        json_dict = json.loads(json_string.text)
        print(json_dict)                    # debug
        print(json_dict['ts'])              # debug
        print(json_dict['wind_u-surface'])  # debug

        for i in range(len(json_dict['ts'])):
            print("Unix_Time =>", json_dict['ts'][i])
            date_time = datetime.datetime.fromtimestamp(json_dict['ts'][i])
            print("Date & Time =>", date_time.strftime('%Y-%m-%d %H:%M:%S'))


    except Exception:
        print("WINDY FAILED")
        raise Exception


    return

# eof
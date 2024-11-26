import requests 
import os

def get_distance(start, end):
    params = {
        "origins": start,
        "destinations": end,
        "key": os.environ.get("API_KEY")
    }
    result = requests.get(os.environ.get("MAPS_API_URL") + "distancematrix/json", params=params) 
    distance = result.json()["rows"][0]["elements"][0]["distance"]["value"]  # distance in meters
    return distance


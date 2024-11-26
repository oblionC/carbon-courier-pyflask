import requests
import os

def compute_route(start, end):
    """Returns an encoded polyline that connects the start and end locations on the map"""
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": os.environ['API_KEY'],
        "X-Goog-FieldMask": "routes.polyline.encodedPolyline"
    }

    data = {
        "origin":{
            "address": start
        },
        "destination":{
            "address": end
        },
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
        "computeAlternativeRoutes": False,
        "routeModifiers": {
            "avoidTolls": True,
            "avoidHighways": False,
            "avoidFerries": False
        },
        "languageCode": "en-US",
        "units": "IMPERIAL"
    }
    response = requests.post(os.environ['ROUTES_API_URL'] + "directions/v2:computeRoutes", json=data, headers=headers)
    response = response.json()
    return response['routes'][0]['polyline']
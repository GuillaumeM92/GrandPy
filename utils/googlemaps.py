import requests

def get_json_response(parsed_question):
    gmaps_json_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + parsed_question + "&key=AIzaSyADzdSV9PVtSJ4QtuK3EgKQWF55egnZR0w&language=fr&region=FR&callback=initMap").json()
    return gmaps_json_response

def get_formatted_address(gmaps_json_response):
    formatted_address = gmaps_json_response['results'][0]['formatted_address']
    return formatted_address

def get_coordinates(gmaps_json_response):
    coordinates = gmaps_json_response['results'][0]['geometry']['location']
    return coordinates

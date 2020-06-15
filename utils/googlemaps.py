import requests

def get_json_response(parsed_question):
    gmaps_json_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + parsed_question + "&key=AIzaSyAY6OVTPCMm5sOekwgVurBENPOdn4h_EtM&language=fr&callback=initMap").json()
    return gmaps_json_response

def get_formatted_address(gmaps_json_response):
    formatted_address = gmaps_json_response['results'][0]['formatted_address']
    return formatted_address

def get_coordinates(gmaps_json_response):
    coordinates = gmaps_json_response['results'][0]['geometry']['location']
    return coordinates

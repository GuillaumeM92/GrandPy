import requests
from env_vars import GOOGLE_API_KEY


def get_json_data(parsed_question):

    try:
        gmaps_json_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + parsed_question +
                                           "&key=" + GOOGLE_API_KEY + "&language=fr&region=FR&callback=initMap").json()

        if gmaps_json_response["status"] == "ZERO_RESULTS":
            return gmaps_json_response["status"]

        else:
            formatted_address = gmaps_json_response['results'][0]['formatted_address']
            coordinates = gmaps_json_response['results'][0]['geometry']['location']
            return(formatted_address, coordinates)

    except Exception as e:
        return ("An exception occured while fetching the Google Maps API data.", e)

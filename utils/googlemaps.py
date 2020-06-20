import requests
from env_vars import GOOGLE_API_KEY


class GmapsFetcher():
    """takes a parsed question and returns a formatted address and its coordinates, using a google maps api call"""

    def __init__(self, parsed_question):
        self.parsed_question = parsed_question

    def get_json_data(self):

        try:
            gmaps_json_response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + self.parsed_question +
                                               "&key=" + GOOGLE_API_KEY + "&language=fr&region=FR&callback=initMap").json()

            if gmaps_json_response["status"] == "ZERO_RESULTS":
                return gmaps_json_response["status"]

            else:
                formatted_address = gmaps_json_response['results'][0]['formatted_address']
                coordinates = gmaps_json_response['results'][0]['geometry']['location']
                return(formatted_address, coordinates)

        except Exception as e:
            return ("An exception occured while fetching the Google Maps API data.", e)

import unittest
from utils.googlemaps import GmapsFetcher
from unittest.mock import patch

# Mock 1
gmaps_mock = {
    "results": [
        {
            "address_components": [
                {
                    "long_name": "55",
                    "short_name": "55",
                    "types": [
                        "street_number"
                    ]
                },
                {
                    "long_name": "Rue du Faubourg Saint-Honoré",
                    "short_name": "Rue du Faubourg Saint-Honoré",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "Paris",
                    "short_name": "Paris",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Arrondissement de Paris",
                    "short_name": "Arrondissement de Paris",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Île-de-France",
                    "short_name": "IDF",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "France",
                    "short_name": "FR",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "75008",
                    "short_name": "75008",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "55 Rue du Faubourg Saint-Honoré, 75008 Paris, France",
            "geometry": {
                "location": {
                    "lat": 48.8704156,
                    "lng": 2.3167539
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 48.8717645802915,
                        "lng": 2.318102880291502
                    },
                    "southwest": {
                        "lat": 48.8690666197085,
                        "lng": 2.315404919708498
                    }
                }
            },
            "place_id": "ChIJR-OmjM5v5kcRIi9Yekb0OC4",
            "plus_code": {
                "compound_code": "V8C8+5P Paris, France",
                "global_code": "8FW4V8C8+5P"
            },
            "types": [
                "establishment",
                "local_government_office",
                "point_of_interest",
                "tourist_attraction"
            ]
        }
    ],
    "status": "OK"
}

# Mock 2
gmaps_no_result_mock = {
    "results": [

    ],
    "status": "ZERO_RESULTS"
}


class TestGoogleMaps(unittest.TestCase):

    def setUp(self):
        self.gmaps_test = GmapsFetcher('openclassrooms')

    def test_get_json_data(self):
        with patch('utils.googlemaps.requests.get') as mocked_get:

            # Test 1 (request successful)
            mocked_get.return_value.ok = True
            mocked_get.return_value.json = lambda: gmaps_mock

            test_result = self.gmaps_test.get_json_data()
            expected_result = (
                "55 Rue du Faubourg Saint-Honoré, 75008 Paris, France", {"lat": 48.8704156, "lng": 2.3167539})
            self.assertEqual(test_result, expected_result)

            # Test 2 (request successful but no matching result)
            mocked_get.return_value.ok = True
            mocked_get.return_value.json = lambda: gmaps_no_result_mock

            test_result = self.gmaps_test.get_json_data()
            expected_result = "ZERO_RESULTS"
            self.assertEqual(test_result, expected_result)

            # Test 3 (request failed)
            mocked_get.return_value.ok = False

            test_result = self.gmaps_test.get_json_data()
            expected_result = "An exception occured while requesting the Google Maps API data."
            self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    unittest.main()

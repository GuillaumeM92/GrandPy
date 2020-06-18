import utils.googlemaps as gmaps

# mock Gmaps api data
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

gmaps_no_result_mock = {
    "results": [

    ],
    "status": "ZERO_RESULTS"
}

parsed_question = "palais elysée"
gibberish_parsed_question = "qsdqsdqsd"


def test_get_json_data():
    assert gmaps.get_json_data(parsed_question) == (
        gmaps_mock['results'][0]['formatted_address'], gmaps_mock['results'][0]['geometry']['location'])
    assert gmaps.get_json_data(
        gibberish_parsed_question) == gmaps_no_result_mock["status"]

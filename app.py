from utils.parser import Parser
from utils.googlemaps import GmapsFetcher, GOOGLE_API_KEY
from utils.mediawiki import MwikiFetcher
import requests
from flask import Flask, jsonify, request, render_template, json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', GMAPS_API_KEY=GOOGLE_API_KEY)


@app.route('/question_handler', methods=['GET', 'POST'])
def question_handler():
    question = request.get_json()
    user_input = question["user_input_value"]

    parser = Parser(user_input)
    parsed_question = parser.parse()

    if parsed_question != "ignore":
        try:
            gmaps = GmapsFetcher(parsed_question)
            gmaps_json_data = gmaps.get_json_data()

            if gmaps_json_data != "ZERO_RESULTS":
                mwiki = MwikiFetcher(gmaps_json_data[1])
                info = mwiki.get_page_id_and_title()
                extract = mwiki.get_extract(info[0], info[1])
                print(extract)
                return jsonify(gmaps_json_data[0], gmaps_json_data[1], extract)
            else:
                return jsonify(gmaps_json_data)

        except (KeyError, ConnectionError):
            return jsonify("error")

    else:
        return jsonify("ignore")


if __name__ == "__main__":
    app.run()

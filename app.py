import utils.parser as parser
import utils.googlemaps as gmaps
import utils.mediawiki as mwiki
import requests
from flask import Flask, jsonify, request, render_template, json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', GMAPS_API_KEY=gmaps.GOOGLE_API_KEY)


@app.route('/question_handler', methods=['GET', 'POST'])
def question_handler():
    question = request.get_json()
    parsed_question = parser.parse(question["user_input_value"])

    if parsed_question != "ignore":
        gmaps_json_data = gmaps.get_json_data(parsed_question)

        print(gmaps_json_data)

        if gmaps_json_data != "ZERO_RESULTS":
            try:
                extract = mwiki.get_extract(gmaps_json_data[1])
                return jsonify(gmaps_json_data[0], gmaps_json_data[1], extract)
            except (KeyError, ConnectionError):
                return jsonify("error")

        else:
            return jsonify("ZERO_RESULTS")
    else:
        return jsonify("ignore")


if __name__ == "__main__":
    app.run()

import utils.parser as parser
import utils.googlemaps as gmaps
import utils.mediawiki as mwiki
import requests
from flask import Flask, jsonify, request, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/question_handler', methods = ['GET', 'POST'])
def question_handler():
	question = parser.get_question()
	
	try:
		parsed_question = parser.parse(question)

		if parsed_question == "ignore":
			return jsonify(parsed_question)
			pass
		else:
			gmaps_json_response = gmaps.get_json_response(parsed_question)

			if gmaps_json_response["status"] == "ZERO_RESULTS":
				return jsonify(gmaps_json_response)
				pass

			else:
				formatted_address = gmaps.get_formatted_address(gmaps_json_response)
				coordinates = gmaps.get_coordinates(gmaps_json_response)
				wiki_coords = mwiki.format_coords(coordinates)
				mwiki_json_response = mwiki.get_json_response(wiki_coords)
				page_id = mwiki.get_page_id(mwiki_json_response)
				title = mwiki.get_title(mwiki_json_response)
				extract = mwiki.get_extract(title, page_id)
				cleaned_extract = mwiki.clean_extract(extract)
				#print(gmaps_json_response)
				return jsonify(formatted_address, coordinates, cleaned_extract)

	except ConnectionError:
		return jsonify(gmaps_json_response, gmaps_json_response, gmaps_json_response)
		#return "Une erreur est survenue. Vérifiez votre connexion puis réessayez."
	except KeyError:
		return jsonify(gmaps_json_response, gmaps_json_response, gmaps_json_response)
		#return "Une erreur innatendue est survenue. Merci de réessayer ultérieurement."

if __name__ == "__main__":
	app.run(debug=True)

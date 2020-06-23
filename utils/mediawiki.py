import requests
import re


class MwikiFetcher():
    """takes coordinates and returns a wikipedia extract, using a media wiki api call"""

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def clean_html(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def get_page_id_and_title(self):
        wiki_coords = ("{}{}{}").format(
            self.coordinates['lat'], '|', self.coordinates['lng'])

        mwiki_response = requests.get(
            "https://fr.wikipedia.org/w/api.php?format=json&action=query&list=geosearch&gscoord=" + wiki_coords + "&gsradius=10000&gslimit=1")

        if mwiki_response.ok:
            mwiki_json_response = mwiki_response.json()

            page_id = str(
                mwiki_json_response['query']['geosearch'][0]['pageid'])
            title = mwiki_json_response['query']['geosearch'][0]['title']

            return (page_id, title)

        else:
            return ("An exception occured while requesting the title and page id from WikiMedia API.")

    def get_extract(self, page_id, title):

        mwiki_response = requests.get(
            "https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exintro&titles=" + title + "&redirects=true")

        if mwiki_response.ok:
            mwiki_json_title_response = mwiki_response.json()

            extract = mwiki_json_title_response['query']['pages'][page_id]['extract']
            cleaned_extract = self.clean_html(extract).replace('\n', '')

            return cleaned_extract

        else:
            return ("An exception occured while requesting the extract from WikiMedia API.")

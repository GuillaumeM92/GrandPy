import requests
import re

def format_coords(coordinates):
    wiki_coords = ("{}{}{}").format(coordinates['lat'], '|', coordinates['lng'])
    return wiki_coords

def get_json_response(wiki_coords):
    mwiki_json_response = requests.get("https://fr.wikipedia.org/w/api.php?format=json&action=query&list=geosearch&gscoord=" + wiki_coords + "&gsradius=10000&gslimit=1").json()
    return mwiki_json_response

def get_page_id(mwiki_json_response):
    page_id = str(mwiki_json_response['query']['geosearch'][0]['pageid'])
    return page_id

def get_title(mwiki_json_response):
    title = mwiki_json_response['query']['geosearch'][0]['title']
    return title

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def get_extract(title, page_id):
    mwiki_json_title_response = requests.get("https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exintro&titles=" + title + "&redirects=true").json()
    extract = mwiki_json_title_response['query']['pages'][page_id]['extract']
    return extract

def clean_extract(extract):
    cleaned_extract = clean_html(extract).replace('\n', '')
    return cleaned_extract
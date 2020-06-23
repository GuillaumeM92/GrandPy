import unittest
from utils.mediawiki import MwikiFetcher
from unittest.mock import patch

# Mock 1
mwiki_geosearch_mock = {
    "batchcomplete": "",
    "query": {
        "geosearch": [
            {
                "pageid": 38724,
                "ns": 0,
                "title": "Palais de l'Élysée",
                "lat": 48.8701444,
                "lon": 2.3164861,
                "dist": 36,
                "primary": ""
            }
        ]
    }
}

# Mock 2
mwiki_extract_mock = {
    "batchcomplete": "",
    "warnings": {
        "extracts": {
            "*": "HTML may be malformed and/or unbalanced and may omit inline images. Use at your own risk. Known problems are listed at https://www.mediawiki.org/wiki/Special:MyLanguage/Extension:TextExtracts#Caveats."
        }
    },
    "query": {
        "pages": {
            "38724": {
                "pageid": 38724,
                "ns": 0,
                "title": "Palais de l'Élysée",
                "extract": "<p>Le <b>palais de l'Élysée</b>, dit <b>l'Élysée</b>, est un ancien hôtel particulier parisien, situé au <abbr class=\"abbr\" title=\"numéro\">n<sup>o</sup></abbr> 55 de la rue du Faubourg-Saint-Honoré, dans le <abbr class=\"abbr\" title=\"Huitième\">8<sup>e</sup></abbr> arrondissement de Paris. Il est le siège de la présidence de la République française et la résidence officielle du président de la République depuis la <abbr class=\"abbr\" title=\"Deuxième\">II<sup>e</sup></abbr> République. \n</p><p>Les médias utilisent par métonymie « l'Élysée » pour désigner les services de la présidence de la République française.\n</p><p>Construit par l'architecte Armand-Claude Mollet en 1720 pour Louis-Henri de La Tour d'Auvergne, comte d'Évreux, le palais de l'Élysée a une histoire illustre : il est offert par Louis XV à sa favorite, la marquise de Pompadour, en 1753, puis devient le palais princier de Joachim Murat, beau-frère de Napoléon <abbr class=\"abbr\" title=\"premier\">I<sup>er</sup></abbr>. Ce dernier en fait en 1805 sa résidence impériale. Son neveu, Napoléon III, premier président de la République française, y habite également à partir de 1848. \n</p><p>L'actuel occupant du palais de l'Élysée est Emmanuel Macron, président de la République depuis le <time class=\"nowrap\" datetime=\"2017-05-14\" data-sort-value=\"2017-05-14\">14 mai 2017</time>.\n</p>",
                "thumbnail": {
                    "source": "https://upload.wikimedia.org/wikipedia/fr/thumb/c/c4/Logo_de_la_pr%C3%A9sidence_de_la_R%C3%A9publique_%282018%29.svg/50px-Logo_de_la_pr%C3%A9sidence_de_la_R%C3%A9publique_%282018%29.svg.png",
                    "width": 50,
                    "height": 50
                },
                "pageimage": "Logo_de_la_présidence_de_la_République_(2018).svg"
            }
        }
    }
}

info = ("38724", "Palais de l'Élysée")

class TestWikiMedia(unittest.TestCase):

    def setUp(self):
        self.mwiki_test = MwikiFetcher({"lat": 48.8704156, "lng": 2.3167539})
        self.page_id = "38724"
        self.title = "Palais de l'Élysée"

    def test_get_page_id_and_title(self):
        with patch('utils.mediawiki.requests.get') as mocked_get:

            # Test 1 (request successful)
            mocked_get.return_value.ok = True
            mocked_get.return_value.json = lambda: mwiki_geosearch_mock

            test_result = self.mwiki_test.get_page_id_and_title()
            expected_result = ("38724", "Palais de l'Élysée")
            self.assertEqual(test_result, expected_result)

            # Test 2 (request failed)
            mocked_get.return_value.ok = False
            test_result = self.mwiki_test.get_page_id_and_title()
            expected_result = "An exception occured while requesting the title and page id from WikiMedia API."
            self.assertEqual(test_result, expected_result)

    def test_get_extract(self):
        with patch('utils.mediawiki.requests.get') as mocked_get:

            # Test 1 (request successful)
            mocked_get.return_value.ok = True
            mocked_get.return_value.json = lambda: mwiki_extract_mock

            test_result = self.mwiki_test.get_extract(self.page_id, self.title)
            expected_result = "Le palais de l'Élysée, dit l'Élysée, est un ancien hôtel particulier parisien, situé au no 55 de la rue du Faubourg-Saint-Honoré, dans le 8e arrondissement de Paris. Il est le siège de la présidence de la République française et la résidence officielle du président de la République depuis la IIe République. Les médias utilisent par métonymie « l'Élysée » pour désigner les services de la présidence de la République française.Construit par l'architecte Armand-Claude Mollet en 1720 pour Louis-Henri de La Tour d'Auvergne, comte d'Évreux, le palais de l'Élysée a une histoire illustre : il est offert par Louis XV à sa favorite, la marquise de Pompadour, en 1753, puis devient le palais princier de Joachim Murat, beau-frère de Napoléon Ier. Ce dernier en fait en 1805 sa résidence impériale. Son neveu, Napoléon III, premier président de la République française, y habite également à partir de 1848. L'actuel occupant du palais de l'Élysée est Emmanuel Macron, président de la République depuis le 14 mai 2017."
            self.assertEqual(test_result, expected_result)

            # Test 2 (request failed)
            mocked_get.return_value.ok = False
            test_result = self.mwiki_test.get_extract(self.page_id, self.title)
            expected_result = "An exception occured while requesting the extract from WikiMedia API."
            self.assertEqual(test_result, expected_result)


if __name__ == '__main__':
    unittest.main()

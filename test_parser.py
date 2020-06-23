import unittest
from utils.parser import Parser

# mock questions list
mock_questions_list = [
    "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
    "A quel endroit se trouve le Palais de l'Elysée ?",
    "où est situé l'opéra de sydney",
    "Je souhaiterais aller au 59 boulevard de Strasbourg, 75010 Paris s'il te plaît.",
    "comment faire pour aller au métro chatelet",
    "Bonjour, quelle est l'adresse de l'hôpital Georges Pompidou?",
    "Hello GrandPy, ça ne te dérange pas de me rappeler où se trouve la ligne Maginot ?",
    "Je dois me rendre boulevard Saint Germain",
    "Où se trouve la fontaine Saint-Michel à Paris ?",
    "Où sont les chutes du Niagara ?",
    "Bonjour bot!! Ou se trouve la Tour Eiffel?",
    "Où se trouve l'Ouganda ?",
    "Où puis-je trouver la Maison Blanche?",
    "Où est posée la statue de la Liberté ?",
    "Salut GrandPy Est-ce que tu connais l'adresse de l'Opéra de Paris?",
    "je voudrais situer le désert de gobie",
    "comment pourrais-je trouver la gare montparnasse ?",
    "Salut GrandPy :) Peux-tu m'indiquer comment me rendre boulevard sébastopol à Paris ? Merci.",
    ""
]

# expected results
expected_results = [
    'openclassrooms',
    'palais elysée',
    'opéra sydney',
    '59 boulevard strasbourg 75010 paris',
    'métro chatelet',
    'hôpital georges pompidou',
    'ligne maginot',
    'boulevard saint germain',
    'fontaine saint michel paris',
    'chutes niagara',
    'tour eiffel',
    'ouganda',
    'maison blanche',
    'statue liberté',
    'opéra paris',
    'désert gobie',
    'gare montparnasse',
    'boulevard sébastopol paris',
    "ignore"
]

class TestWikiMedia(unittest.TestCase):

    def test_parse_auto(self):
        iterator = 0

        for questions in mock_questions_list:
            self.parser_test = Parser(questions)
            test_result = self.parser_test.parse()

            expected_result = expected_results[iterator]
            self.assertEqual(test_result, expected_result)

            iterator += 1


if __name__ == '__main__':
    unittest.main()

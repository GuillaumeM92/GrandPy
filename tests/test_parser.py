import utils.parser as parser

# mock questions list
question00 = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
question01 = "A quel endroit se trouve le Palais de l'Elysée ?"
question02 = "où est situé l'opéra de sydney"
question03 = "Je souhaiterais aller au 59 boulevard de Strasbourg, 75010 Paris s'il te plaît."
question04 = "comment faire pour aller au métro chatelet"
question05 = "Bonjour, quelle est l'adresse de l'hôpital Georges Pompidou?"
question06 = "Hello GrandPy, ça ne te dérange pas de me rappeler où se trouve la ligne Maginot ?"
question07 = "Je dois me rendre boulevard Saint Germain"
question08 = "Où se trouve la fontaine Saint-Michel à Paris ?"
question09 = "Où sont les chutes du Niagara ?"
question10 = "Bonjour bot!! Ou se trouve la Tour Eiffel?"
question11 = "Où se trouve l'Ouganda ?"
question12 = "Où puis-je trouver la Maison Blanche?"
question13 = "Où est posée la statue de la Liberté ?"
question14 = "Salut GrandPy Est-ce que tu connais l'adresse de l'Opéra de Paris?"
question15 = "je voudrais situer le désert de gobie"
question16 = "comment pourrais-je trouver la gare montparnasse ?"
question17 = "Salut GrandPy :) Peux-tu m'indiquer comment me rendre boulevard sébastopol à Paris ? Merci."


def test_parse():
    assert parser.parse(question00) == 'openclassrooms'
    assert parser.parse(question01) == 'palais elysée'
    assert parser.parse(question02) == 'opéra sydney'
    assert parser.parse(question03) == '59 boulevard strasbourg 75010 paris'
    assert parser.parse(question04) == 'métro chatelet'
    assert parser.parse(question05) == 'hôpital georges pompidou'
    assert parser.parse(question06) == 'ligne maginot'
    assert parser.parse(question07) == 'boulevard saint germain'
    assert parser.parse(question08) == 'fontaine saint michel paris'
    assert parser.parse(question09) == 'chutes niagara'
    assert parser.parse(question10) == 'tour eiffel'
    assert parser.parse(question11) == 'ouganda'
    assert parser.parse(question12) == 'maison blanche'
    assert parser.parse(question13) == 'statue liberté'
    assert parser.parse(question14) == 'opéra paris'
    assert parser.parse(question15) == 'désert gobie'
    assert parser.parse(question16) == 'gare montparnasse'
    assert parser.parse(question17) == 'boulevard sébastopol paris'
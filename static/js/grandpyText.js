const answer1 = ["Tout de suite mon grand ! ",
"Pas de problème ! ",
"Laisse-moi voir ça... ",
"Donne moi une minute... ",
"GrandPy s'en occuppe tout de suite ! ",
"Pas de soucis, je sais où ça se trouve... "];


const answer2 = ["L'adresse que tu cherches est la suivante : ",
"Voilà ton adresse : ",
"Voici l'adresse que tu m'as demandée : ",
"Et voilà ! C'est par ici : ",
"J'ai trouvé ! C'est ici : ",
"C'est juste ici : "];

const anecdote = ["A ce propos, j'ai une petite anecdote à ce sujet qui pourrait t'intéresser... ",
"Permet-moi de t'en dire davantage à ce sujet... ",
"Voilà quelques petites précisions concernant ce lieu... ",
"Je parie que tu ne savais pas que... ",
"A ce sujet... ",
"Savais-tu que... "
];

function getRandomText(array) {
	var randomText = array[Math.floor(Math.random() * array.length)];
	return randomText
}
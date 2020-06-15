# GrandPy
Repository pour le Projet 7 de mon parcours de formation "Développeur d'Applications Python" chez OpenClassrooms.  
  
Adresse du site : https://grandpyweb.herokuapp.com/

## Description du Projet
This is a web application build with **Flask** to help user to find an address and learn more about the story of this location.

## Fonctionnalités
* Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
* Utilisation de l'API de Google Maps et celle de Media Wiki.
* Affichage d'un plan Google Maps intégré à la page.
* Réponses variées de la part de GrandPy.

## Parcours utilisateur
L'utilisateur ouvre son navigateur et se rend sur grandpyweb.herokuapp.com :
* L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée.
* Le message s'affiche dans la zone de chat qui affiche tous les messages échangés. Une icône apparaît pour indiquer que GrandPy est en train de réfléchir.
* Puis un nouveau message apparaît : "Je m'en occuppe ! La voici : 7 cité Paradis, 75010 Paris." En-dessous, une anecdote tirée de Wikipedia apparaît, ainsi qu'une carte Google Maps avec un marqueur indiquant l'adresse demandée.

## APIs
Les API suivantes ont été utilisées pour ce projet :  
* [Google maps](https://developers.google.com/maps/get-started/)  
* [Medi Wiki](https://www.mediawiki.org/wiki/API:Main_page) APIs.
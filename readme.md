Afin de pouvoir tourner sur un serveur de déploiment, flask a besoin d'un serveur WSGI.
waitress permet d'avoir un serveur WSGI.

Pour lancer le projet sur le serveur render : waitress-serve --port=8000 app:app

Pour lancer le projet en local debug: python ./app.py

https://orbitwatch.onrender.com
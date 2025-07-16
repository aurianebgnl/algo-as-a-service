
## dependencies
fastapi : le framework pour créer l'API.
uvicorn : le serveur web léger et rapide qui exécute l'API

## lancement du serveur
uvicorn main:app --reload --port 8888
--reload : mode développement, redémarrage auto du serveur 

## tester avec Swagger UI
http://localhost:8888/docs
ou http://localhost:8888/redoc

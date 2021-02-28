# rest

**Project Installation**

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

```
## Run the app

    python3 manage.py runserver

## Get list of Games
### Request

`GET /games/`

    to view all games.
    >http://localhost:8000/games/
    
    must take a search param to request to search for games.
    >http://localhost:8000/games/?search=search**
    
    to categorize games, must take a filter param for categories, and a search param to search for the game.
    **http://localhost:8000/games/categorized/?filter=filter&search=search**
    
    to view owned games if there is.
    **http://localhost:8000/games/ownedgames/**


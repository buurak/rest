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

    http://localhost:8000/games/
    
`GET /search/`
    
    http://localhost:8000/games/?search=search

`GET /games/categorized/`

    http://localhost:8000/games/categorized/?filter=filter&search=search

`GET /games/ownedgames/`

    http://localhost:8000/games/ownedgames/



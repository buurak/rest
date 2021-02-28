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

    http://localhost:8000/games/?search=search

    http://localhost:8000/games/categorized/?filter=Dövüş&search=search

    http://localhost:8000/games/ownedgames/


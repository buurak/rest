# rest

**Project Installation**

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

```
## Run the app

    python3 manage.py runserver
    
    
## Login
### Request

`POST`

    http://localhost:8000/api/token/
     
    http://localhost:8000/api/refresh/token/


## Register
### Request

`POST`

    http://localhost:8000/register/


## Get list of Games
### Request

`GET`

    http://localhost:8000/games/
     
    http://localhost:8000/games/?search=search

    http://localhost:8000/games/categorized/?filter=filter&search=search

    
   
## Get list of Owned Games
### Request

`GET`

    http://localhost:8000/games/ownedgames/


## Basket
### Request

`GET`

    http://localhost:8000/basket/
    
    
## Add a game to Basket
### Request
`POST`
     
    http://localhost:8000/addtobasket/?game_id=game_id
    
    
## Remove a game from Basket
### Request
`POST`
     
    http://localhost:8000/removefrombasket/?game_id=game_id
    
    
## Checkout
### Request

`POST`
    http://localhost:8000/games/checkout/



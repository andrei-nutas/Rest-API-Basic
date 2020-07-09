from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from securityWithObjects import authenticate, identity

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db


# a resource is just a thing that our Api can return and create, they are usually mapped in database tables as well

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# we need to tell SQLAlchemy where to find teh data.db file
# what we are saying is that the SQLAlchemy database is going to live at teh root folder of our project
# INTERESTING: it doesn't have to be sqlite it can be Oracle, MySql, etc and it will just work
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# in order to know when an object had changed but not been saved to the db Flask SQLALCHEMY was tracking every change we made to the SQLALCHEMY session that took resources.
# we are now turning this off because SQLALCHEMY has it's own tracker which is a bi better.
# this turns off the Flask SQLALCHEMY modification tracker NOT the SQLALCHEMY modification tracker
# this is only changing the extensions behaviour and not the underlying SQLALCHEMY behaviour.

app.secret_key = 'jose' 
#to encript and then understand what was encrypted you need a secret_key (in general the scret key need to be long and complicated)

api = Api(app)
# the api will allow us to easily add resources to the app
# the api works with resources and every resource has to be a class
# the new classes must inherit at some point down the inheretence line from the class Resource

@app.before_first_request
#this will affect the method below it and it will run it before the first request into this app
def create_tables():
    db.create_all()
# this will create all the tables unless they exist already 

jwt = JWT(app, authenticate, identity) # /auth


    
api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(UserRegister, '/register')
# this replaces the endpoint decoration @app.route
# in essence it tells our server that the Item resource can be accesed from this endpoint: http://127.0.0.1:5000/item/Pen

if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 5000)
# we use this so the app doesn't run if we end up importing app in app.py in any other file
# this is important because when we import we don't want to run the app but just gain access to its functions and objects
# only the file that you run is __main__


# jwt stands for json web token
# it is an obfucation of data
# what it does is to encode data, it allows for privacy unless the source has a particular decription key
# we will use jwt with user IDs
# the user will send us a User name and password, and we will send them a jwt
# this jwt will be the user ID
# when the client has the JWT they can send it to us with any request they make
# this will tell us that they are authentificated, aka that they previously logged in





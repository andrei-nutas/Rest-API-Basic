from app import app
from db import db

db.init_app(app)

@app.before_first_request
#this will affect the method below it and it will run it before the first request into this app
def create_tables():
    db.create_all()
# this will create all the tables unless they exist already 
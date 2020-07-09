# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:32:48 2020

@author: andreinutas
"""
# the class UserModel from hereis not a resource because our API cannot retrieve data from this class or send this class as ajson representation
# this class is a helper that is used to store some data about the user
# it is also a helper that contains a couple of methods that allows us to easily retrieve user objects from a data base
# the API client interacts and deals with resouces
# however when we deal internally in our code with a user we are using the model not the resource
# the model has the code that allows our program to do what it has to do
# model = helper, that gives more flexibility without poluting the resources with which the clients interact with 
# model = internal representation
# resource = external representation


from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # we have told SQLAlchemy the three columns that this model is going to have
    # when it comes to saving into the data base it is only going to look for these three properties
    # the properties self.x must mach the columns for them to be saved to the db
    # if we have other properties this will not give us an error
    # the properties will exist in the object but it will not be in any way related to the database
    
    def __init__(self, username, password):
        # we no longer use an _id in the object because id is a primary key that is autoincrementing
        # whenever we insert a new row in the database, the SQL engine will automatically assign an id for us
        # as a resurt we do not need to specify the id as it is automatically given
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        #check ItemModel for explenation

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

# this user model here is an API
# This Api exposes at the moment two endpoints, two methods
# This API, these two methods are an interface for other parts of our program to interact with the user thing 
# And that includes retriving from and writing into the database
# as long as we don't change the API we don't have to worry about ou changes anywhere else in the code
# What this means is that this API is used in the security file
# we changed the impelmentation of our UserModel but security.py doesn't care because it is just calling the methods
# as long as the methods return the same thing, everything is fine
# Our RestAPIs are the same. we have our endpoints and the web and mobile app interacting with it doesn't care if it's written in Python or Ruby
# All it cares is that it's getting the data back that it requested in the same formats that it expects


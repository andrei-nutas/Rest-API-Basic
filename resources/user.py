# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 23:24:22 2020

@author: andreinutas
"""

# we will use the sqlite with our API in order to sign users in
# ==> we will be able to log in with our sqlite

# =====> we are going to store users in sqlite and 
# when the user calls the /auth endpoint we are going to retrieve the sqlite from the database

# we will use the data that was created by running test.py

import sqlite3
# this will give our User class the ability to interact with SQLite

from flask_restful import Resource, reqparse

from models.user import UserModel


# with this we will allow our users to sign up
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = 'This field cannot be blank')
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = 'This field cannot be blank')
    #will parse through the JSON of the request to make sure the user name and passowrd are there
    
    
    # the Userregister inherits from Resource so we can add it to the API using flask_restful
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400    
        
        user = UserModel(**data) # **data unpacks data to : data['username'], data['password']
        
        user.save_to_db()
        
        return {'message': 'User was succesfully created.'}, 201
        #by using flask_restful we can register a user by just using post
        
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
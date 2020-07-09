# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 23:09:21 2020

@author: andreinutas 
"""
from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # we are lookign in th data base after the user
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)  


    









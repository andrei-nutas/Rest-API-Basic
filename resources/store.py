# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:37:55 2020

@author: andreinutas
"""

from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()       
        return {'message' : 'Store does not exist'}, 404     

    def post(self, name):    
        if StoreModel.find_by_name(name):
            return {'message': 'Store already exists'}, 400
        
        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'},500
        
        return store.json(), 201
    
    # not making a put becausea a store only has a name so changing the name is basically changing everything about the store
    # hence we can consider it creating a new store
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return{'message':'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
     
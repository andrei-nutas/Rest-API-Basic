# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:23:37 2020

@author: andreinutas
"""
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

# we are moving our items into the data base
# hence we will retrive and create items in the data base

class Item(Resource):
    parser = reqparse.RequestParser()
    # we use this to ensure that only some elements can be passedin through the json payload
        
    parser.add_argument('price',
                        type = float,
                        required = True,
                        help = "This field can't be left blank"
                        )
    parser.add_argument('store_id',
                        type = int,
                        required = True,
                        help = "Every item needs a store id"
                        )
    
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()       
        return {'message' : 'Item does not exist'}, 404
     

    def post(self, name): 
        if ItemModel.find_by_name(name):
            return {'message': 'Item already exists'}, 400
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name, **data)
       
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured'},500
        
        return item.json(), 201
    
    def put(self, name):
        # put is an idempotent Item, this means you can call put N times and get the same output
        # put can be used to create an Item or update an existing Item
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name,  **data)
        
        item.save_to_db()        
        
        return item.json(), 201
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return{'message':'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
    
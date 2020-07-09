# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:41:06 2020

@author: andreinutas
"""
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # the foreign key allows us to link two differnet tables, i.e. the items with the stores
    # the id in the storeis a primary key and in the item a foreign key
    # we can then know which items belongs to which store by referencing the store_id in the item
    # we can later aggregate all the items in the appropirate store by using said key
    # as long as we will have items that use the id of a certain store, we will not be able to delete the store
    # the database engine will not allow it because there are foreign key references
    # all items that use that specific store need to be deleted or moved to another store before you can delete sai store
    
    store = db.relationship('StoreModel')
    # this sees that we have a store id
    # therefore we can find a store in the DB that matches the store.id in its id
    
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json (self):
        return {'name': self.name, 'price': self.price}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # we have the ItemModel, which is the class which is a type of SQLAlchemy model
        # then we say we want to query the model, now SQLAlchemy knows that we are going to be building a query on the db
        # then we filter_by (name=name), which is doing: SELECT * FROM __tablename__ WHERE name =name
        # and it does all that without the connect cursor, etc
        # in addition befor we had to select the first row in order to find only the one element that matches the name 
        # in order to incorporate that we end with .first
        # this does the following: SELECT * FROM __tablename__ WHERE name = name LIMIT 1
        # also, the data gets converted into an ItemModel object            
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # SQLAlchemy can directly translate from object to row in a DB so we don't have to tell it what row data to insert
        # we just have to tell it to insert this object into the db
        # the session is a collection of objects that we are going to add to the data base
        # we can also add multiple objects to the sessionm, and write them all at once
        
        # when we retrieve an object from the DB that hasa particular ID
        # then we can change the object's name and all we have to do is to add it to the session and comit it again
        # and SQLAlchemy will do an unpdate instead of an insert
        
        # thus the insert method here is actually useful for both update and insert
        # hence we will rename the method to save to db
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    
    
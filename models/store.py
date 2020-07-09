# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 01:18:36 2020

@author: andreinutas
"""

from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    items = db.relationship('ItemModel', lazy='dynamic')

    # we are doing here a backrefference
    # this allows the store to see which items from the items table have a store.id eaqual to its own id
    # this variable is a list because this items could be many items. It is a many to one relationship
    
    def __init__(self, name):
        self.name = name
    
    def json (self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        # becuase we usedlazy = 'dynamic', self.items no longer raises a list of items
        # now it is a query builder thta has the ability to look into the items table
        # hence we use .all() to retrieve all of the items
        # everytime we call the json method we have to run the query
        # we are trading off btw speed of creation of the store and speed of calling the json method
        # without lazy and .all the call would be faster
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    
    
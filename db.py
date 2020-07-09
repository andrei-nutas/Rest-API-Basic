# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:43:13 2020

@author: andreinutas
"""

from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy ()
# we have an object that is SQLAlchemy
# this is going to link with our Flask app and will look at all of the objects that we tell it to
# it will then allow us to map those objects to rows in a data base
# i.e. when we create an item model object that has a column called name and a column called price
# it will allow us to very easily put that object into a data base
# putting an object into the data base means saving an objects properties into the data base; SQLAlchemy excels at this





# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:41:32 2020

@author: andreinutas
"""
# here we are making sure that we are creating the appropriate tables

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
# in order to make id an auto-incrementing column we have to use INTEGER PRIMARY KEY
cursor.execute(create_table)

create_table = "CREATE TABLE items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

connection.commit()

connection.close()
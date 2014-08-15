#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('nerf.db')

with con:
    cur = con.cursor()    
    cur.execute("""CREATE TABLE IF NOT EXISTS Games(
        Id INTEGER PRIMARY KEY, 
        Mod TEXT,
        CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        Player1 TEXT,
        Player2 TEXT,
        Score1 INT,
        Score2 INT,
        Closed INT)""")

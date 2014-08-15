#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import sqlite3 as lite

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    con = lite.connect('nerf.db')
    cur = con.cursor()
    last_game_id = cur.lastrowid
    cur.execute(
        "SELECT Score1 FROM Games WHERE id=?", last_game_id
    )
    data = dict(cur.fetchall())
except lite.Error, e:
    print 'Connection to nerf.db impossible'

while True:
    if(GPIO.input(23) ==1):
        data['Score1'] += 1
        cur.execute(
            "UPDATE Games SET Score1=? WHERE Id=?", (data['Score1'], last_game_id)
        )        
        con.commit()
GPIO.cleanup()
if con:
    con.close()

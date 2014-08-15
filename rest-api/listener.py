#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import sqlite3 as lite

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    con = lite.connect('nerf.db')
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute('SELECT id, Score1 FROM Games WHERE id=(SELECT max(id) FROM Games)')
    data = cur.fetchone()
except lite.Error, e:
    print 'Connection to nerf.db impossible'
    print e.args[0]

while True:
    if(GPIO.input(23) ==1):
        data[1] += 1
        cur.execute(
            "UPDATE Games SET Score1=? WHERE Id=?", (data[1], data[0])
        )
        con.commit()
GPIO.cleanup()
if con:
    con.close()

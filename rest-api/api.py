#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask import jsonify
import sqlite3 as lite

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# http://IP:5000/create/PLAYSERNAME1/PLAYERNMAE2
@app.route('/create/<user1>/<user2>')
def create_game(user1, user2):
    try:
        con = lite.connect('nerf.db')
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Games VALUES(?, ?, ?, ?)", (user1, user2, 0, 0)
        )
        lid = cur.lastrowid
        return jsonify(id=lid)
    except lite.Error, e:
        return jsonify(error=e.args[0])
    finally:
        if con:
            con.close() 

# http://IP:5000/game/ID
@app.route('/game/<game_id>')
def get_score(game_id):
    try:
        con = lite.connect('nerf.db')
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM Games WHERE id=?", game_id
        )
        return jsonify(dict(cur.fetchall()))
    except lite.Error, e:
        return jsonify(error=e.args[0])
    finally:
        if con:
            con.close() 

if __name__ == "__main__":
    app.run(host='0.0.0.0')

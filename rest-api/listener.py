#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import sqlite3 as lite
import sys, time
from raspledstrip.ledstrip import *
from bootstrap import *

# Stop the game if 
# - Timer is out
# - Single mod : Score1 >= 32
# - Double mod : Score1 || Score2 >= 16
def is_done(game_data):
  if game_data['Mod'] == 'single':
    ts = int(time.time())
    if ts - game_data['CreatedAt'] > 120:
      stop_game(game_data['Id'])
      return True
    elif game_data['Score1'] >= 32:
      stop_game(game_data['Id'])
      return True
  if game_data['Mod'] == 'double':
    if game_data['Score1'] >= 16 || game_data['Score2'] >= 16:
      stop_game(game_data['Id'])
      return True
  return False

# Stop a game from the database 
# and reset lights ?
def stop_game(con, game_id):
  cur = con.cursor()
  cur.execute(
    "UPDATE Games SET Closed=1 WHERE Id=?", game_id)
  )
  con.commit()

# Return the latests game in database
def get_last_game(con):
  cur = con.cursor()
  cur.execute('SELECT * FROM Games WHERE id=(SELECT max(id) FROM Games)')
  return cur.fetchone()

def add_pts_to(con, game_id, player, pts):
  cur = con.cursor()
  cur.execute(
    "UPDATE Games SET Score%s=%s WHERE Id=%s" % (player, pts, game_id)
  )
  con.commit()

# Return the latests game in database
def get_last_game(con):
  cur = con.cursor()
  cur.execute('SELECT * FROM Games WHERE id=(SELECT max(id) FROM Games)')
  return cur.fetchone()

if __name__ == "__main__":
  #        P1   P2
  # 8pts = 25 + 22
  # 5pts = 23 + 17
  # 3pts = 18 + 4 
  # Pin 24 == reset 
  inputs = [18, 25, 23, 17, 22, 4]
  GPIO.setmode(GPIO.BCM)
  for idx in inputs:
    GPIO.setup(idx, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
  
  # Get the data of the last game
  try:
    con = lite.connect('nerf.db')
    con.row_factory = lite.Row
  except lite.Error, e:
    print 'Connection to nerf.db impossible'
    print e.args[0]



if __name__ == "__main__":
  #        P1   P2
  # 8pts = 25 + 22
  # 5pts = 23 + 17
  # 3pts = 18 + 4 
  # Pin 24 == reset 
  inputs = [18, 25, 23, 17, 22, 4]
  GPIO.setmode(GPIO.BCM)
  for idx in inputs:
    GPIO.setup(idx, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
  
  # Get the data of the last game
  try:
    con = lite.connect('nerf.db')
    con.row_factory = lite.Row
  except lite.Error, e:
    print 'Connection to nerf.db impossible'
    print e.args[0]

  need_new_game = 0
  current_game = get_last_game(con)

  while True:
    if need_new_game == 1:
      current_game = get_last_game(con)
    # if the current game is closed we wait for a new one
    if current_game['Closed'] == 1:
      need_new_game = 1
      continue
    
    # we check if a target has been hited
    for idx in inputs:
      if(GPIO.input(idx) == 1):
        # 24 == exit button !
        if idx == 24:
          stop_game(con, current_game['Id'])
          break
        else:
          # Add point to player + update db
          # Need : pin == points + which player is shooting + which LED
          switch(n) {
              case 18:
              # Add 3pts to P1
              add_pts_to(con, current_game['Id'], 1, 3)
              break;
              case 25:
              # Add 8pts to P1
              add_pts_to(con, current_game['Id'], 1, 8)
              break;
              case 23:
              # Add 5pts to P1
              add_pts_to(con, current_game['Id'], 1, 5)
              break;
              case 17:
              # Add 5pts to P2
              add_pts_to(con, current_game['Id'], 2, 5)
              break;
              case 22:
              # Add 8pts to P2
              add_pts_to(con, current_game['Id'], 2, 8)
              break;
              case 4:
              # Add 3pts to P2
              add_pts_to(con, current_game['Id'], 1, 3)
              break;
          }
          # Check game is done
          is_done(current_game)
  
  if con:
    con.close()
  GPIO.cleanup()

######
#  led.fillRGB(0,255,0,idx,idx)
#  GPIO.cleanup()
#  if con:
#      con.close()
#  
#  led = LEDStrip(32)
#  led.fillRGB(0,0,0,0,32)
#  
#  GPIO.setmode(GPIO.BCM)
#  
#  anim = LarsonScanner(led, Color(255, 0, 0))
#  for i in range(led.lastIndex*12):
#          anim.step()
#          led.update()
#          #sleep(0.03)
#  
#  led.fillOff()
#  
#  
#  while True:
#          for idx in inputs:
#                  if(GPIO.input(idx) == 1):
#                          if idx == 24:
#                                  sys.exit()
#                          led.fillRGB(0,255,0,idx,idx)
#          led.update()
#          led.fillRGB(0,0,0,0,32)

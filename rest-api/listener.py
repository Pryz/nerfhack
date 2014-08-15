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
def is_done(con, game_data):
  print game_data['Mod']
  print game_data['Score1'], '  ',game_data['Score2']
  print
  if game_data['Mod'] == 'single':
    ts = int(time.time())
    if ts - game_data['CreatedAt'] > 120:
      stop_game(con, game_data['Id'])
      return True
    elif game_data['Score1'] >= 32:
      stop_game(con, game_data['Id'])
      return True
  if game_data['Mod'] == 'double':
    if game_data['Score1'] >= 16 or game_data['Score2'] >= 16:
      print "Closing"
      if game_data['Score1'] >= 16:
        for i in range(0, 5): 
          led.fillRGB(0, 0, 0, 0, 31)
          led.update()
          sleep(0.2)
          led.fillRGB(0, 255, 0, 0, 31)
          led.update()
	  sleep(0.2)
      if game_data['Score2'] >= 16:
        for i in range(0, 5): 
          led.fillRGB(0, 0, 0, 0, 31)
          led.update()
          sleep(0.2)
          led.fillRGB(0, 0, 255, 0, 31)
          led.update()
	  sleep(0.2)
      stop_game(con, game_data['Id'])
      return True
  return False

# Stop a game from the database 
# and reset lights ?
def stop_game(con, game_id):
  print 'Closing game' 
  cur = con.cursor()
  cur.execute(
    "UPDATE Games SET Closed=1 WHERE Id=%s" % game_id
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

def check_if_led():
  for idx in inputs:
    if(GPIO.input(idx) == 1):
      return 1
  return 0

def create_dummy_game(con):
  cur = con.cursor()
  cur.execute(
      "INSERT INTO Games(Mod, Player1, Player2, Score1, Score2) VALUES('double', 'dummy1', 'dummy2' ,0 ,0)",
  )
  con.commit()
  return cur.lastrowid

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
  GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

  # Starting Lights
  #anim = LarsonScanner(led, Color(255, 0, 0))
  #for i in range(led.lastIndex*12):
  #        anim.step()
  #        led.update()
  #        #sleep(0.03)
  led.fillOff()
  
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
    if(GPIO.input(24) == 1):
      # 24 == exit button !
      print 'press my button'
      targets_up=0
      for idx in inputs:
        if(GPIO.input(idx) == 1):
          targets_up=1

      if targets_up > 0:
	print 'the button see a target'
        for i in range(0, 5): 
          led.fillRGB(0, 0, 0, 0, 31)
          led.update()
          sleep(0.2)
          led.fillRGB(255, 0, 0, 0, 31)
          led.update()
	  sleep(0.2)
      else: 
        print 'the button see des trucs'
        if current_game['Closed'] == 0:
          stop_game(con, current_game['Id'])
        led.fillRGB(0, 0, 0, 0, 31)
        create_dummy_game(con)
      led.update()
    if need_new_game == 1:
      print "Check for a new Game"
      current_game = get_last_game(con)
    # if the current game is closed we wait for a new one
    if current_game['Closed'] == 1:
      print "The curent Game is closed"
      need_new_game = 1
      continue
    
    # we check if a target has been hited
    P1 = 0
    P2 = 0
    for idx in inputs:
      if(GPIO.input(idx) == 1):
	# print "%s down !" % idx
        # 24 == exit button !
        if idx == 24:
	  print 'press my button'
          stop_game(con, current_game['Id'])
          #led.fillOff()
	  led.fillRGB(0, 0, 0, 0, 31)
          led.update()
          break
        else:
          # Add point to player + update db
          # Need : pin == points + which player is shooting + which LED
          if idx == 18:
            # Add 3pts to P1
            P1 += 3
          elif idx == 25:
            # Add 8pts to P1
            P1 += 8
          elif idx == 23:
            # Add 5pts to P1
            P1 += 5
          elif idx == 17:
            # Add 5pts to P2
            P2 += 5
          elif idx == 22:
            # Add 8pts to P2
            P2 += 8
          elif idx == 4:
            # Add 3pts to P2
            P2 += 3
    add_pts_to(con, current_game['Id'], 1, P1)
    add_pts_to(con, current_game['Id'], 2, P2)
    print P1," ",P2
    if P1 > 0:
    	led.fillRGB(0, 255, 0, 0, P1 - 1 )
    led.fillRGB(0, 0, 255, 32 - P2, 31)
    led.update()

    led.fillRGB(0,0,0,0,32)
    # Check game is done
    is_done(con, current_game)
  
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

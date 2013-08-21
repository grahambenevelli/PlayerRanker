#!/usr/bin/env python

# -------
# imports
# -------

import sys
import os

APP_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(APP_PATH + '/library/xlrd-0.9.2')
sys.path.append(APP_PATH + '/app/player')
sys.path.append(APP_PATH + '/app/league')
sys.path.append(APP_PATH + '/app')

import xlrd
import pprint

from Player import Player
from LeagueFactory import LeagueFactory
from CsvManager import CsvManager

# ----
# main
# ----

leagueFactory = LeagueFactory()
league = leagueFactory.getLeague(sys.stdin, sys.stdout)

workbook = xlrd.open_workbook(APP_PATH + '/resources/stats/20130815.xls')

worksheet = workbook.sheet_by_name('2013 proj - season')

num_rows = worksheet.nrows - 1
curr_row = 29

row = worksheet.row(curr_row)
keys = [x.value for x in row]

players = {'QB': [], 'RB': [], 'WR': [], 'TE': []}

# Collect players
while curr_row < num_rows:
	curr_row += 1
	row = worksheet.row(curr_row)
	row = dict(zip(keys, row))
	if row['Pos'].value == 'PK' or row['Pos'].value == 'ST':
		continue
	player = league.getPlayer(row['Player'].value)
	if player is None:
		continue

	player.setStat('Pass Yds', row['Y Pa'].value)
	player.setStat('Pass TD', row['TD P'].value)
	player.setStat('Pass Int', row['Int'].value)
	player.setStat('Rush Yards', row['Y Run'].value)
	player.setStat('Rush TD', row['TD Run'].value)
	player.setStat('Rec Yards', row['Y Rec'].value)
	player.setStat('Rec TD', row['TD Rec'].value)
	player.setStat('Ret TD', row['TD Ret'].value)
	
csvManager = CsvManager()

csvManager.printPlayers(league)
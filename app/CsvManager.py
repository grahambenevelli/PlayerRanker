#!/usr/bin/env python

import os
import sys

APP_PATH = os.path.dirname(os.path.realpath(__file__))

class CsvManager:

	def printPlayers(self, league):
		positions = iter(['QB', 'RB', 'WR', 'TE'])

		for pos in positions:
			#f = open( APP_PATH + "/../resources/players/" + pos + "Stats.csv", "w" )
			f = sys.stdout
			columns = league.players.getColumns();
			f.write(",".join(columns) + "\n")
			for player in league.players:
				if player.getPosition() == pos:
					f.write(player.toCsv(columns) + "\n")
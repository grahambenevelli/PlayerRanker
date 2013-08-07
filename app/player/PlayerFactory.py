#!/usr/bin/env python

import os
import sys

sys.path.append('app/player')

from Player import Player

class PlayerFactory:

	APP_PATH = os.path.dirname(os.path.realpath(__file__))

	def __init__(self):
		self.positions = iter(['QB', 'RB', 'WR', 'TE', 'DEF'])
		self.lines = iter([])

	def __iter__(self):
		return self

	def next(self):
		try:
			return self.createPlayer(self.lines.next())
		except StopIteration:
			self.setUpFile()
			return self.next()

	def setUpFile(self):
		self.lines = open( self.APP_PATH + "/../../resources/players/" + self.positions.next() + ".csv", "r" )

	def createPlayer(self, line):
		data = line.split(',')
		return Player(data[0], data[1], float(data[2]))


#!/usr/bin/env python

import sys
import os

from PlayerFactory import PlayerFactory

class PlayerStorage:

	def __init__(self):
		self.playerFactory = PlayerFactory()
		self.importAllPlayers()

	def importAllPlayers(self):
		self.playersByPos = {}
		self.players = []
		while True:
			try:
				player = self.playerFactory.next()
				if player.position not in self.playersByPos:
					self.playersByPos[player.position] = []
				self.playersByPos[player.position].append(player)
				self.players.append(player)
			except StopIteration:
				return

	def sort(self, values, numPlayers):
		self.players.sort(key=lambda x: x.getValue(values), reverse=True)
		for pos in self.playersByPos:
			self.setAverages(pos, numPlayers[pos], self.playersByPos[pos])
		self.players.sort(key=lambda x: x.getValue(values), reverse=True)

	def setAverages(self, pos, num, players):
		total = 0
		for i in range(num):
			total += self.playersByPos[pos][i].getPoints()
		average = total / num
		for player in self.playersByPos[pos]:
			player.setAverage(average)

	def top(self, pos = 'players', num = None):
		if num is None:
			num = 10

		if pos == None or pos == 'players':
			return self.players[:num]
		else:
			return self.playersByPos[pos][:num]

	def getPlayer(self, name):
		for p in self.players:
			if p.getName() == name:
				return p

	def eliminatePlayer(self, player):
		self.players.remove(player)
		self.playersByPos[player.getPosition()].remove(player)
		
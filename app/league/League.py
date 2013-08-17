#!/usr/bin/env python

import os
import sys

sys.path.append('app/team')

from Team import Team

class League:
	
	def __init__(self, name, teams, positions, values):
		self.name = name
		self.values = values
		self.asc = 1

		self.teams = []
		for team in teams:
			self.teams.append(Team(team, positions))
		self.positions = positions
		self.teamIndex = 0
		self.positionsLeft = {}
		for pos in positions:
			self.positionsLeft[pos] = self.positions[pos] * len(self.teams)

	def getNumPlayersToFill(self, pos):
		return self.positionsLeft[pos]

	def draft(self, player):
		self.positionsLeft[player.getPosition()] -= 1
		self.teams[self.teamIndex].draft(player)
		self.updateIndex()

	def updateIndex(self):
		if self.asc == 1 and self.teamIndex == len(self.teams) - 1:
			self.asc = 0
		elif self.asc == 1:
			self.teamIndex += 1
		elif self.teamIndex == 0:
			self.asc = 1
		else:
			self.teamIndex -= 1


	def printTeam(self, name):
		team = None
		for t in self.teams:
			if t.getName() == name:
				team = t
				break
		return str(team)

	def getCurrentTeam(self):
		return self.teams[self.teamIndex].getName()

	def getValues(self):
		return self.values
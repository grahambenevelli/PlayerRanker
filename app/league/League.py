#!/usr/bin/env python

import os
import sys

sys.path.append('app/team')

from Team import Team

class League:
	
	def __init__(self, name, teams, positions):
		self.name = name
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
		self.teamIndex = (self.teamIndex + 1) % len(self.teams)

	def printTeam(self, name):
		for t in self.teams:
			if t.getName() == name:
				team = t
				break
		return str(team)

	def getCurrentTeam(self):
		return self.teams[self.teamIndex].getName()

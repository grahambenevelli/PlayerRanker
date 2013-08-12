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

	def getNumPlayersToFill(self, pos):
		return self.positions[pos] * len(self.teams)

	def draft(self, player):
		self.teams[self.teamIndex].draft(player)
		self.teamIndex += 1

	def printTeam(self, name):
		for t in self.teams:
			if t.getName() == name:
				team = t
				break
		return str(team)

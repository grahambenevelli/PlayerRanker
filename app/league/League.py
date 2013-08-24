#!/usr/bin/env python

import os
import sys
import difflib

sys.path.append('app/team')
sys.path.append('app/player')

from PlayerStorage import PlayerStorage

from Team import Team

class League:
	
	def __init__(self, name, teams, positions, values, keepers = {}):
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

		self.players = PlayerStorage()
		self.players.sort(self.getValues(), self.getNumPlayersToFill())
		self.eliminateKeepers(keepers)

	def eliminateKeepers(self, keepers = {}):
		for team in keepers:
			players = keepers[team]
			team = self.getTeam(team)
			for player in players:
				self.draft(self.getPlayer(player), team)

	def getNumPlayersToFill(self):
		return self.positionsLeft

	def draft(self, player, team = None):
		self.players.eliminatePlayer(player)
		self.positionsLeft[player.getPosition()] -= 1
		if team is None:
			team = self.getCurrentTeam()
		team.draft(player)
		self.updateIndex()
		self.players.sort(self.getValues(), self.getNumPlayersToFill())		

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
		return self.teams[self.teamIndex]

	def getValues(self):
		return self.values

	def top(self, pos, num):
		return self.players.top(pos, num)

	def getPlayer(self, name):
		return self.players.getPlayer(name)

	def getTeam(self, teamName):
		for team in self.teams:
			if teamName == team.getName():
				return team

	def getPossiblePlayers(self, name):
		return difflib.get_close_matches(name, [x.getName() for x in self.players.players])

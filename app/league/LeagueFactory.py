#!/usr/bin/env python

import os
import sys
import json
from pprint import pprint

from League import League

class LeagueFactory:

	APP_PATH = os.path.dirname(os.path.realpath(__file__))

	def getLeague(self, reader, writer):
		self.reader = reader
		self.writer = writer
		leagueNames = []
		for root, dirs, files in os.walk("./resources/league"):
			for f in files:
				leagueNames.append(f)
		return self.pickLeague(leagueNames)

	def pickLeague(self, leagueNames):
		while True:
			self.printLeague(leagueNames)
			line = self.reader.readline()
			if not line.strip().isdigit() or int(line) > len(leagueNames) + 1 or int(line) < 1:
				continue
			if int(line) == len(leagueNames) + 1:
				teams = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8', 'Team9', 'Team10', 'Team11', 'Team12']
				positions = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'DEF': 1}
				return League("Default", teams, positions)
			return self.buildLeagueFromFile(leagueNames[int(line) - 1])

	def buildLeagueFromFile(self, file):
		lines = open( self.APP_PATH + "/../../resources/league/" + file, "r" )
		json_data = open( self.APP_PATH + "/../../resources/league/" + file, "r" )
		data = json.load(json_data)
		json_data.close()

		return League("Default", data['teams'], data['positions'])

	def printLeague(self, leagueNames):
		index = 1
		for name in leagueNames:
			self.writer.write(str(index) + ": " + name + "\n")
			index += 1
		self.writer.write(str(index) + ": default\n\n")
		self.writer.write("Pick league by number: ")

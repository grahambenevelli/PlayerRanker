#!/usr/bin/env python

import os
import sys

from League import League

class LeagueFactory:

	def getLeague(self):
		teams = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8', 'Team9', 'Team10', 'Team11', 'Team12']
		positions = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'DEF': 1}
		return League(teams, positions)
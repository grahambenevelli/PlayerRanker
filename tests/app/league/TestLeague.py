#!/usr/bin/env python

# -------
# imports
# -------

import sys

sys.path.append('app/league')

import StringIO
import unittest

from League import League

# ----------
# TestRanker
# ----------

class TestLeague (unittest.TestCase) :

	teams = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8']
	positions = {'qb': 1, 'rb': 2, 'wr': 3, 'te': 1, 'def': 1}

	def setUp(self):
		self.league = League(self.teams, self.positions)

	def test_init(self):
		self.assertEquals(self.teams, self.league.teams)
		self.assertEquals(self.positions, self.league.positions)

	def test_getNumPlayersToFill(self):
		self.assertEquals(8, self.league.getNumPlayersToFill('qb'))
		self.assertEquals(16, self.league.getNumPlayersToFill('rb'))
		self.assertEquals(24, self.league.getNumPlayersToFill('wr'))
		self.assertEquals(8, self.league.getNumPlayersToFill('te'))
		self.assertEquals(8, self.league.getNumPlayersToFill('def'))
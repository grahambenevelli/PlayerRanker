#!/usr/bin/env python

import os
import sys

class League:
	
	def __init__(self, teams, positions):
		self.teams = teams
		self.positions = positions

	def getNumPlayersToFill(self, pos):
		return self.positions[pos] * len(self.teams)

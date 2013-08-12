#!/usr/bin/env python

import os
import sys

class Team:

	def __init__(self, name, positions):
		self.name = name
		self.roster = {}
		for position in positions:
			for x in range(positions[position]):
				self.roster[position] = []

	def __str__(self):
		ret = self.name + "\n"
		for spot in self.roster:
			ret += spot + ": \t"
			for player in self.roster[spot]:
				ret += str(player)
			if len(self.roster[spot]) == 0:
				ret += "\n"
		return ret

	def getName(self):
		return self.name

	def draft(self, player):
		self.roster[player.getPosition()].append(player)
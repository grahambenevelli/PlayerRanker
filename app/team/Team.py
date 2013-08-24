#!/usr/bin/env python

import os
import sys

class Team:

	def __init__(self, name, positions):
		self.positions = positions
		self.name = name
		self.roster = {}
		for position in positions:
			for x in range(positions[position]):
				self.roster[position] = []

	def __str__(self):
		ret = self.name + "\n"
		for pos in self.positions:
			for x in range(self.positions[pos]):
				ret += pos + ": \t"
				if x < len(self.roster[pos]):
					ret += self.roster[pos][x].getName()
				ret += "\n"
		return ret

	def getName(self):
		return self.name

	def draft(self, player):
		self.roster[player.getPosition()].append(player)
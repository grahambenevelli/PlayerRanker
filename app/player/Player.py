#!/usr/bin/env python

import os
import sys
import math

APP_PATH = os.path.dirname(os.path.realpath(__file__))

class Player:

	def __init__(self, name, team, position, stats):
		self.name = name
		self.team = team
		self.position = position
		self.stats = stats
		self.points = None
		self.value = None
		self.deviation = None

	def __eq__(self, other):
		return (isinstance(other, self.__class__)
			and self.name == other.name
			and self.position == other.position
			and (not hasattr(self, 'average') or self.average == other.average)
			and (not hasattr(self, 'initialAverage') or self.initialAverage == other.initialAverage))

	def __str__(self):
		return self.name + " " + self.position + ": " + str(self.getPoints()) + " " + str(self.getValue())

	def getName(self):
		return self.name

	def getPosition(self):
		return self.position

	def getPoints(self):
		return self.points

	def getTeam(self):
		return self.team

	def setAverage(self, average, first = False):
		if first or not hasattr(self, 'initialAverage'):
			self.initialAverage = average
		self.average = average

	def getDeviation(self):
		return math.fabs(self.points - self.average)

	def setDeviation(self, dev):
		self.deviation = dev

	def getValue(self, values = None):
		if values is None:
			return self.value
		if self.points is None:
			self.points = self.mapPoints(self.stats, values)
		if not hasattr(self, 'average'):
			return self.points
		if not hasattr(self, 'deviation'):
			self.value = ((self.points - self.average) + (self.points - self.initialAverage)) / 2
			return self.value
		self.value = ((self.points - self.average + self.deviation) + (self.points - self.initialAverage + self.deviation)) / 2
		return self.value

	def mapPoints(self, stats, values):
		points = 0
		for key in stats:
			try:
				points += float(stats[key]) * float(values[key])
			except KeyError:
				continue
		return points

	def getStats(self):
		return ["Name", "Team"] + [value for value in self.stats if value != "Fan Pts\n"]

	def setStat(self, stat, value):
		self.stats[stat] = value

	def toCsv(self, columns):
		row = []
		for col in columns:
			if col == 'Name':
				row.append(self.getName())
				continue
			if col == 'Team':
				row.append(self.getTeam())
				continue
			row.append(str(self.stats[col]).strip())
		return ",".join(row)

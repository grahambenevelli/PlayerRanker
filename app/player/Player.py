#!/usr/bin/env python

import os
import sys

APP_PATH = os.path.dirname(os.path.realpath(__file__))

class Player:

	def __init__(self, name, team, position, stats):
		self.name = name
		self.team = team
		self.position = position
		self.stats = stats
		self.points = None
		self.value = None

	def __eq__(self, other):
		return (isinstance(other, self.__class__)
			and self.name == other.name
			and self.position == other.position
			and (not hasattr(self, 'average') or self.average == other.average)
			and (not hasattr(self, 'initialAverage') or self.initialAverage == other.initialAverage))

	def __str__(self):
		return self.name + " " + self.position + ": " + str(self.getValue())

	def getName(self):
		return self.name

	def getPosition(self):
		return self.position

	def getPoints(self):
		return self.points

	def setAverage(self, average, first = False):
		if first or not hasattr(self, 'initialAverage'):
			self.initialAverage = average
		self.average = average

	def getValue(self, values = None):
		if values is None:
			return self.value
		if self.points is None:
			self.points = self.mapPoints(self.stats, values)
		if not hasattr(self, 'average'):
			return self.points
		self.value = ((self.points - self.average) + (self.points - self.initialAverage)) / 2
		return self.value

	def mapPoints(self, stats, values):
		points = 0
		for key in stats:
			try:
				points += float(stats[key]) * float(values[key])
			except KeyError:
				continue
		return points
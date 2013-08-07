#!/usr/bin/env python

# -------
# imports
# -------

import os
import sys

sys.path.append('app')
sys.path.append('app/player')

import StringIO
import unittest

from Player import Player
from PlayerFactory import PlayerFactory

# ----------
# TestRanker
# ----------

class TestPlayerFactory (unittest.TestCase):

	def setUp(self):
		self.factory = PlayerFactory()

	def test_Init(self):
		self.assertEquals('QB', self.factory.positions.next())
		self.assertEquals('RB', self.factory.positions.next())
		self.assertEquals('WR', self.factory.positions.next())
		self.assertEquals('TE', self.factory.positions.next())
		self.assertEquals('DEF', self.factory.positions.next())
		self.assertRaises(StopIteration, self.factory.positions.next)
		self.assertRaises(StopIteration, self.factory.lines.next)

	def test_Iter(self):
		self.assertEquals(self.factory, iter(self.factory))

	def test_setUpFile(self):
		self.factory.setUpFile()
		file = open( self.factory.APP_PATH + "/../../resources/players/QB.csv", "r" )
		self.assertEquals(file.name, self.factory.lines.name)

	def test_createPlayer(self):
		name = 'Arian Foster'
		position = 'RB'
		points = 127.5
		line = name + ',' + position + ',' + str(points)

		expected = Player(name, position, points)
		actual = self.factory.createPlayer(line)

		self.assertEquals(expected.name, actual.name)
		self.assertEquals(expected.position, actual.position)
		self.assertEquals(expected.points, actual.points)

	def test_next(self):
		player = self.factory.next()
		self.assertEquals('Aaron Rodgers', player.name)
		self.assertEquals('QB', player.position)
		self.assertEquals(344.59, player.points)

		for x in range(40):
			player = self.factory.next()

		self.assertEquals('Adrian Peterson', player.name)
		self.assertEquals('RB', player.position)
		self.assertEquals(284.03, player.points)


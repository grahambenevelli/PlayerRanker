#!/usr/bin/env python

import sys

sys.path.append('app/player')

import StringIO
import unittest

from Player import Player

# ----------
# TestRanker
# ----------

class TestPlayer (unittest.TestCase):

    name = 'Test Name'
    position = 'QB'
    points = 122.88

    def setUp(self):
        self.player = Player(self.name, self.position, self.points)

    def test_PlayerInitTest (self):
        self.assertEquals(self.name, self.player.name)
        self.assertEquals(self.position, self.player.position)
        self.assertEquals(self.points, self.player.points)

    def test_eq(self):
        player1 = Player("Test Name", "QB", 123.45)
        player2 = Player("Test Name", "QB", 123.45)

        self.assertEquals(player1, player2)

        player1 = Player("Test Name", "QB", 123.46)

        self.assertNotEquals(player1, player2)

    def test_getValue(self):
        self.assertEquals(self.points, self.player.getValue())

        self.player.setAverage(120.00)
        self.assertTrue(abs(2.88 - self.player.getValue()) < 0.0001)

    def test_setAverage(self):
        self.player.setAverage(120.00, True)
        self.assertEquals(120.00, self.player.average)
        self.assertEquals(120.00, self.player.initialAverage)

        self.player.setAverage(110.00)
        self.assertEquals(110.00, self.player.average)
        self.assertEquals(120.00, self.player.initialAverage)




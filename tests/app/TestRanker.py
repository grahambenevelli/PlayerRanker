#!/usr/bin/env python

# -------
# imports
# -------

import sys

sys.path.append('app')
sys.path.append('app/player')
sys.path.append('app/league')

import StringIO
import unittest

from Ranker import Ranker
from Player import Player
from League import League

# ----------
# TestRanker
# ----------

class TestRanker (unittest.TestCase) :

    def test_init (self):
        teams = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8']
        positions = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'DEF': 1}

        league = League(teams, positions)
        writer = StringIO.StringIO()
        reader = StringIO.StringIO('')
        ranker = Ranker(league, writer, reader)
        self.assertIsInstance(ranker.writer, StringIO.StringIO)
        self.assertIsInstance(ranker.reader, StringIO.StringIO)
        
        qb = Player('Aaron Rodgers', 'QB', 344.59)
        rb = Player('Adrian Peterson', 'RB', 284.03)
        wr = Player('Calvin Johnson', 'WR', 210.8)
        te = Player('Rob Gronkowski', 'TE', 185.03)
        df = Player('Chicago', 'DEF', 218.48)

        self.assertEquals(qb, ranker.playersByPos['QB'][0])
        self.assertEquals(rb, ranker.playersByPos['RB'][0])
        self.assertEquals(wr, ranker.playersByPos['WR'][0])
        self.assertEquals(te, ranker.playersByPos['TE'][0])
        self.assertEquals(df, ranker.playersByPos['DEF'][0])


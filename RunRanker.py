#!/usr/bin/env python

# -------
# imports
# -------

import sys
import os

APP_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(APP_PATH + '/app')
sys.path.append(APP_PATH + '/app/league')
sys.path.append(APP_PATH + '/app/player')

from Ranker import Ranker
from LeagueFactory import LeagueFactory
from PlayerFactory import PlayerFactory
from PlayerEditor import PlayerEditor

# ----
# main
# ----

leagueFactory = LeagueFactory()
league = leagueFactory.getLeague(sys.stdin, sys.stdout)

# playerEditor = PlayerEditor(sys.stdin, sys.stdout, league)
# playerEditor.run()

ranker = Ranker(league, sys.stdin, sys.stdout)
ranker.run()
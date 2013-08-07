#!/usr/bin/env python

# -------
# imports
# -------

import sys
import os

sys.path.append("./tests/app")
sys.path.append("./tests/app/player")
sys.path.append("./tests/app/league")

import StringIO
import unittest

# To create a new test File add import your test here
import TestRanker
import TestPlayer
import TestPlayerFactory
import TestLeague

# ----
# main
# ----

print "Testing Player Ranker"

# Create Loader and Suite
loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(TestRanker)

# Add tests to Suite
suite.addTests(loader.loadTestsFromModule(TestPlayer))
suite.addTests(loader.loadTestsFromModule(TestPlayerFactory))
suite.addTests(loader.loadTestsFromModule(TestLeague))

# Run tests
unittest.TextTestRunner(verbosity=2).run(suite)

print "Done."

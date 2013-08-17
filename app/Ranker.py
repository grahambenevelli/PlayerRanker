#!/usr/bin/env python

import os
import sys

APP_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(APP_PATH + '/player')

from PlayerFactory import PlayerFactory

APP_PATH = os.path.dirname(os.path.realpath(__file__))

class Ranker:

    def __init__(self, league, reader, writer):
        self.league = league
        self.reader = reader
        self.writer = writer
        self.playerFactory = PlayerFactory()
        self.importAllPlayers()
        self.sort()

    def run(self):
        while True:
            self.writer.write(">>>> ")

            line = self.reader.readline()
            parts = line.split()
            command = parts[0]
            param = parts[1:]

            if command == 'top':
                self.top(param)
            if command == 'draft':
                self.draft(param)
            if command == 'print':
                self.printTeam(param)
            if command == 'current':
                self.writer.write(self.league.getCurrentTeam());
            if command == 'quit' or command == 'exit':
                return

            self.writer.write("\n")

    def sort(self):
        self.players.sort(key=lambda x: x.getValue(self.league.getValues()), reverse=True)
        for pos in self.playersByPos:
            self.setAverages(pos, self.league.getNumPlayersToFill(pos), self.playersByPos[pos])
        self.players.sort(key=lambda x: x.getValue(self.league.getValues()), reverse=True)

    def setAverages(self, pos, num, players):
        total = 0
        for i in range(num):
            total += self.playersByPos[pos][i].getPoints()
        average = total / num
        for player in self.playersByPos[pos]:
            player.setAverage(average)

    def importAllPlayers(self):
        self.playersByPos = {}
        self.players = []
        while True:
            try:
                player = self.playerFactory.next()
                if player.position not in self.playersByPos:
                    self.playersByPos[player.position] = []
                self.playersByPos[player.position].append(player)
                self.players.append(player)
            except StopIteration:
                return

    def top(self, param):
        pos = None
        num = None

        if len(param) >= 2:
            pos = param[1].upper()

        if len(param) >= 1:
            if not param[0].isdigit():
                self.writer.write("top not formatted correctly")
            num = int(param[0])

        if num is None:
            num = 10

        if pos == None or pos == 'players':
            for player in self.players[:num]:
                self.writer.write(str(player) + "\n")
        else:
            try:
                for player in self.playersByPos[pos][:num]:
                    self.writer.write(str(player) + "\n")
            except KeyError:
                self.writer.write("top not formatted correctly")

    def draft(self, param):
        name = " ".join(param)
        for p in self.players:
            if p.getName() == name:
                player = p
                break
        self.players = [s for s in self.players if s.getName() != name]
        self.playersByPos[player.getPosition()] = [s for s in self.playersByPos[player.getPosition()] if s.getName() != name]
        
        self.writer.write(player.getName() + " drafted by " + self.league.getCurrentTeam())
        self.league.draft(player)

        self.sort()

    def printTeam(self, param):
        name = " ".join(param)
        if name == "current":
            name = self.league.getCurrentTeam()
        self.writer.write(self.league.printTeam(name))

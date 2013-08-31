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

    def run(self):
        while True:
            self.writer.write(">>>> ")

            line = self.reader.readline()
            if line == "\n":
                continue
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
                self.writer.write(self.league.getCurrentTeam().getName());
            if command == 'quit' or command == 'exit':
                return

            self.writer.write("\n")

    def top(self, param):
        pos = None
        num = None

        if len(param) >= 2:
            pos = param[1].upper()

        if len(param) >= 1:
            if not param[0].isdigit():
                self.writer.write("top not formatted correctly")
                return
            num = int(param[0])

        try:
            for player in self.league.top(pos, num):
                self.writer.write(str(player) + "\n")
        except KeyError:
            self.writer.write("top not formatted correctly")

    def draft(self, param):
        name = " ".join(param)
        possibles = self.league.getPossiblePlayers(name)
        while True:
            if len(possibles) == 0:
                self.writer.write("No one by that names exists")
                return
            if len(possibles) == 1:
                name = possibles[0]
                break
            for x in range(len(possibles)):
                self.writer.write(str(x + 1) + ": ")
                self.writer.write(possibles[x] + "\n")
            self.writer.write("Do you mean one of these: ")
            line = self.reader.readline()
            print line
            if line.strip().isdigit():
                print "true"
            else:
                print "false"
            if line.strip().isdigit() and int(line) > 0 and int(line) <= len(possibles):
                name = possibles[int(line) - 1]
                break


        player = self.league.getPlayer(name)

        if player == None:
            self.writer.write("Player by name " + name + " doesn't exist")
            return

        self.writer.write(player.getName() + " drafted by " + self.league.getCurrentTeam().getName() + "\n")
        self.league.draft(player)
        self.writer.write(self.league.getCurrentTeam().getName() + " now on clock")
        
    def printTeam(self, param):
        name = " ".join(param)
        if name == "current":
            name = self.league.getCurrentTeam().getName()
        self.writer.write(self.league.printTeam(name))

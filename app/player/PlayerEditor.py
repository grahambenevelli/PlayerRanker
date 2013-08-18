#!/usr/bin/env python

import os
import sys

class PlayerEditor:

	def __init__(self, reader, writer, league):
		self.league = league
		self.reader = reader
		self.writer = writer

	def run(self):
		while True:
			self.writer.write(">>>> ")

			line = self.reader.readline()
			parts = line.split()
			command = parts[0]
			param = parts[1:]

			if command == 'edit':
				self.editPlayer(param)
			if command == 'draft':
				return
			if command == 'quit' or command == 'exit':
				sys.exit(0)

			self.writer.write("\n")

	def editPlayer(self, param):
		name = " ".join(param)
		player = self.league.getPlayer(name)
		stats = player.getStats()
		for stat in stats:
			if stat == "Fan Pts\n":
				continue
			self.writer.write(stat + " currently set to " + str(stats[stat]) + ", change to: ")
			value = self.reader.readline()
			if value != "\n":
				player.setStat(stat, float(value))
				self.writer.write(stat + " set to " + value)
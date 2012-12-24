#!/usr/bin/python2

import fontFirst

font = fontFirst.fontFirst

class LedScreen:
	def __init__(self, lines):
		self.lines = lines
		self.screen = []
		for n in range(lines):
			self.screen.append('')
	def __repr__(self):
		return 'LED screen: ' + str(self.lines) + ' lines, ' + str(self.getWidth()) + ' px wide'
	def clear(self):
		for n in range(self.lines):
			self.screen[n] = ''
	def display(self):
		return self.screen
	def displayRange(self, start, length):
		tempScreen = []
		end = start + length - 1
		for n in range(self.lines):
			tempScreen.append(self.screen[n][start:end])
		return tempScreen
	def getWidth(self):
		return len(self.screen[0])
	def addChar(self, pxList):
		charLines = len(pxList)
		if charLines > self.lines:
			raise ValueError('Too many lines in character.')
		charWidth = 0
		for line in pxList:
			if len(line) > charWidth:
				charWidth = len(line)
		if self.getWidth() != 0:
			for n in range(self.lines):
				self.screen[n] += ' '
		for n in range(self.lines):
			if n < len(pxList):
				toAdd = pxList[n]
			else:
				toAdd = ''
			while len(toAdd) < charWidth:
				toAdd += ' '
			self.screen[n] += toAdd

screen = LedScreen(8)

text = 'Dead Beef Cafe'
for char in text:
	screen.addChar(font[char])

print screen
scrLines = screen.display()
for line in scrLines:
	print line

screen.clear()
charsToPrint = sorted(font)
charsToPrint.remove(' ')
for char in charsToPrint:
	screen.addChar(font[char])
print screen

scrPos = 0
dispLen = 80

while scrPos < screen.getWidth():
	scrLines = screen.displayRange(scrPos, dispLen)
	for line in scrLines:
		print line
	scrPos += dispLen
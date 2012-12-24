#!/usr/bin/python2

"""
A test program to demonstrate LedScreen and scrolling text on an LED display.
"""

import os
import sys
import fontFirst
from time import sleep

# font is a dict of characters that can be fed into LedScreen
# font['A'] gives you the character for capital A
FONT = fontFirst.fontFirst

# clears the terminal
# taken from https://gist.github.com/4368100
def clear_screen(numlines=100):
    """Clear the console.

    numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('cls')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)

# LedScreen is an object that simulates an LED matrix display of specified
#     height
# Example:
#     myScreen = LedScreen(8) # creates an LED screen of 8 vertical pixels
# Add characters to the right side of the screen with LedScreen.addChar(char)
# Characters must be a list of pixels, usually from a font dict.
class LedScreen:
    """An object that simulates an LED matrix display."""
    def __init__(self, lines):
        """Initialize the screen object with a specified height."""
        self.lines = lines
        self.screen = []
        while lines > 0:
            self.screen.append('')
            lines -= 1
    def __repr__(self):
        """Return a string with information about the screen object."""
        return 'LED screen: ' + str(self.lines) + ' lines, ' + \
               str(self.get_width()) + ' px wide'
    def clear(self):
        """Clear all pixels on the screen object, setting its width to 0."""
        for n in range(self.lines):
            self.screen[n] = ''
    def display(self):
        """Return all pixels on the screen as a list of horizontal lines of
            pixels."""
        return self.screen
    def display_range(self, start, length):
        """Return all pixels on the screen as a list of horizontal lines of
           pixels, starting at a specific position and ending after a specific
           number of pixels."""
        tempScreen = []
        end = start + length - 1
        if start >= self.get_width():
            spaces = ' ' * length
            for n in range(self.lines):
                tempScreen.append(spaces)
            return tempScreen
        elif start < 0:
            for n in range(self.lines):
                tempScreen.append(self.screen[n][0:length - 1])
            #while start < 0:
            #   for n in range(self.lines):
            #       tempScreen[n] = ' ' + tempScreen[n][:len(tempScreen[n]) - 1]
            #   start += 1
            diff = -start
            if diff > length:
                diff = length
            spaces = ' ' * diff
            for n in range(self.lines):
                tempScreen[n] = spaces + tempScreen[n][:length - diff]
            return tempScreen
        else:
            for n in range(self.lines):
                tempScreen.append(self.screen[n][start:end])
            return tempScreen
    def get_width(self):
        """Return the screen's width in pixels."""
        return len(self.screen[0])
    def add_char(self, pxList):
        """Add a character's pixels to the right side of the screen."""
        charLines = len(pxList)
        if charLines > self.lines:
            raise ValueError('Too many lines in character.')
        charWidth = 0
        for line in pxList:
            if len(line) > charWidth:
                charWidth = len(line)
        if self.get_width() != 0:
            for n in range(self.lines):
                self.screen[n] += ' '
        for n in range(self.lines):
            if n < len(pxList):
                toAdd = pxList[n]
            else:
                toAdd = ''
            if len(toAdd) < charWidth:
                diff = charWidth - len(toAdd)
                toAdd += ' ' * diff
            self.screen[n] += toAdd
    def add_string(self, strToAdd, font):
        """Adds a string to the right side of the screen using a specified
           font."""
        for char in strToAdd:
            self.add_char(font[char])

screen = LedScreen(8)

if len(sys.argv) > 1:
    fullStr = sys.argv[1]
else:
    charsToPrint = sorted(FONT)
    charsToPrint.remove(' ')
    fullStr = ''.join(charsToPrint)

screen.add_string(fullStr, FONT)

dispLen = 32
scrStart = -dispLen
scrEnd = screen.get_width() + 1

scrPos = scrStart
scrWidth = screen.get_width()
while scrPos < scrEnd:
    clear_screen()
    print scrPos, '/', scrWidth
    scrLines = screen.display_range(scrPos, dispLen)
    for line in scrLines:
        print line
    sleep(0.02)
    scrPos += 1
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
        for line_num in range(self.lines):
            self.screen[line_num] = ''
    def display(self):
        """Return all pixels on the screen as a list of horizontal lines of
            pixels."""
        return self.screen
    def display_range(self, start, length):
        """Return all pixels on the screen as a list of horizontal lines of
           pixels, starting at a specific position and ending after a specific
           number of pixels."""
        temp_screen = []
        end = start + length - 1
        if start >= self.get_width():
            spaces = ' ' * length
            for line_num in range(self.lines):
                temp_screen.append(spaces)
            return temp_screen
        elif start < 0:
            for line_num in range(self.lines):
                temp_screen.append(self.screen[line_num][0:length - 1])
            #while start < 0:
            #   for n in range(self.lines):
            #       temp_screen[n] = ' ' + \
            #           temp_screen[n][:len(temp_screen[n]) - 1]
            #   start += 1
            diff = -start
            if diff > length:
                diff = length
            spaces = ' ' * diff
            for line_num in range(self.lines):
                temp_screen[line_num] = spaces + \
                    temp_screen[line_num][:length - diff]
            return temp_screen
        else:
            for line_num in range(self.lines):
                temp_screen.append(self.screen[line_num][start:end])
            return temp_screen
    def get_width(self):
        """Return the screen's width in pixels."""
        return len(self.screen[0])
    def add_char(self, px_list):
        """Add a character's pixels to the right side of the screen."""
        char_lines = len(px_list)
        if char_lines > self.lines:
            raise ValueError('Too many lines in character.')
        char_width = 0
        for line in px_list:
            if len(line) > char_width:
                char_width = len(line)
        if self.get_width() != 0:
            for line_num in range(self.lines):
                self.screen[line_num] += ' '
        for line_num in range(self.lines):
            if line_num < len(px_list):
                to_add = px_list[line_num]
            else:
                to_add = ''
            if len(to_add) < char_width:
                diff = char_width - len(to_add)
                to_add += ' ' * diff
            self.screen[line_num] += to_add
    def add_string(self, str_to_add, font):
        """Adds a string to the right side of the screen using a specified
           font."""
        for char in str_to_add:
            self.add_char(font[char])

SCREEN = LedScreen(8)

if len(sys.argv) > 1:
    FULL_STR = sys.argv[1]
else:
    CHARS_TO_PRINT = sorted(FONT)
    CHARS_TO_PRINT.remove(' ')
    FULL_STR = ''.join(CHARS_TO_PRINT)

SCREEN.add_string(FULL_STR, FONT)

DISP_LEN = 32
SCR_START = -DISP_LEN
SCR_END = SCREEN.get_width() + 1

SCR_POS = SCR_START
SCR_WIDTH = SCREEN.get_width()
while SCR_POS < SCR_END:
    clear_screen()
    print SCR_POS, '/', SCR_WIDTH
    SCREEN_LINES = SCREEN.display_range(SCR_POS, DISP_LEN)
    for one_line in SCREEN_LINES:
        print one_line
    sleep(0.02)
    SCR_POS += 1
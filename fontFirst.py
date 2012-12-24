#!/usr/bin/python2

import math

fontFirst = {}

fontFirst['A'] = [\
	'  #',
	'  #',
	' # #',
	' # #',
	' ###',
	'#   #',
	'#   #']

fontFirst['B'] = [\
	'### ',
	'#  #',
	'#  #',
	'###',
	'#  #',
	'#  #',
	'###']

fontFirst['C'] = [\
	' ###',
	'#   #',
	'#',
	'#',
	'#',
	'#   #',
	' ###']

fontFirst['D'] = [\
	'###',
	'#  #',
	'#  #',
	'#  #',
	'#  #',
	'#  #',
	'###']

fontFirst['E'] = [\
	'####',
	'#',
	'#',
	'###',
	'#',
	'#',
	'####']

fontFirst['F'] = [\
	'####',
	'#',
	'#',
	'###',
	'#',
	'#',
	'#']

fontFirst['G'] = [\
	' ###',
	'#   #',
	'#',
	'# ##',
	'#   #',
	'#   #',
	' ###']

fontFirst['H'] = [\
	'#  #',
	'#  #',
	'#  #',
	'####',
	'#  #',
	'#  #',
	'#  #']

if __name__ == '__main__':
	for char in fontFirst:
		charRaw = fontFirst[char]
		for line in charRaw:
			print line
		print
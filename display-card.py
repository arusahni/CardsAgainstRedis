#!/usr/bin/python
from termcolor import colored
import string

def displayCard(color,text):
	text = "|" + text
	textLength = len(text)
	print textLength
	text = colored(text, color,attrs=['reverse'])
	x = 1
	dashes = "-"

	while x < textLength:
		dashes = dashes + "-"
		x += 1
	dash1 = colored(dashes,color)
	print dash1
	print colored("|\n|\n|\n|",color)
	print string.center(text,30)
	print colored("|\n|\n|\n|",color)
	dash2 = colored(dashes,color)
	print dash2
	return

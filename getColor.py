#getColor.py
#!/usr/bin/env python

# Maak een dictionary
# Neem namen van landen van function getCountryList
# geef willekeurig kleuren aan landen
# keys van dictionary zijn landen en values zijn willekeurig waarde
# return dictionary

from getCountryList import getCountryList	
from random import randrange

def getColor():
	landColor = {}
	landen = getCountryList()
	for i in landen:
		setRed = randrange(256)
		setGreen = randrange(256)
		setBlue = randrange(256)
		kleur = setRed, setGreen, setBlue
		landColor[i] = kleur
	return landColor

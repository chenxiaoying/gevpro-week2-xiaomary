#flag_color.py
#!/usr/bin/env python

# We weten niet hoe je een functie aanroept vanuit een class

from PyQt4 import QtCore, QtGui
from random import randrange
from getCountryList import getCountryList

class FlagColor(QtGui.QColor):
	def __init__(self):
		super(FlagColor,self).__init__()
		self.initUI
		
	def initUI(self):
		self.landColor = {}
		landen = getCountryList()
		for i in landen:
			self.setRed = randrange(256)
			self.setGreen = randrange(256)
			self.setBlue = randrange(256)
			self.kleur = self.setRed, self.setGreen, self.setBlue
			self.landColor[i] = self.kleur
		return self.landColor
		

#country.py
#!/usr/bin/env python
# Maryam Mohamed en Xiaoying Chen

from PyQt4 import QtCore, QtGui
import sys
from getCountryList import getCountryList
from getColor import getColor

class Country(QtGui.QWidget):
	def __init__(self):
		super(Country,self).__init__()
		self.setGeometry(200, 200, 400, 200)
		self.setWindowTitle('Country')
		
		# Print introductie
		self.intro = QtGui.QLabel('Kies een land',self)
		self.intro.move(110,25)
		
		self.initUI()
			
	def initUI(self):
		# Maak een comboBox
		self.combo = QtGui.QComboBox(self)
		self.combo.addItems(getCountryList())
		self.combo.move(100,50)
		
		# Maak een label voor 'Hello'
		self.greet = QtGui.QLabel(self)
		self.greet.resize(400,50)
		self.greet.move(110,100)
		
		# Roep de functie getColor aan
		self.lc = getColor()
		
		# Reageren op de signalen
		self.combo.currentIndexChanged.connect(self.updateUI)

	def updateUI(self):
		# Neem de waarde van de gekozen land op
		self.land = self.combo.currentText()
		
		# Signalen sturen
		self.greet.setText(self.__str__())
		
		# Als gekozen land in de dictionary staat, geef de kleur van de land als background kleur
		if self.land in self.lc.keys():
			a = unicode(self.land)
			kleur = self.lc[a]
			self.setStyleSheet("background-color: rgb{}".format(kleur))


	def __str__(self):
		return 'Hello from {}'.format(self.land)
		

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    counry = Country()
    counry.show()
    app.exec_()

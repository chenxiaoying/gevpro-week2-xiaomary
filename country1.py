#!/usr/bin/env python

class Country:
	def __init__(self,country):
		self.country = country
		
	def __str__(self):
		return 'Hello from {}'.format(self.country)
		
if __name__ == "__main__":
	print(Country("Holland"))
	

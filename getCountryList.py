def getCountryList():
	countrylist = []
	infile = open('countries_list.txt','r')
	for line in infile:
		countrylist.append(line.rstrip())
	return countrylist


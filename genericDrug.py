#!/usr/bin/python

import wikipedia

error = int()

def genericDrug():

	brandName = raw_input("Enter brand name of drug: ")

	search = wikipedia.search(brandName, results=1)

	genericPage = wikipedia.page(search)


	def response (genericPage):
		genericName = genericPage.title
		print(genericName)
	
	summarytext = wikipedia.summary(genericPage)

	if summarytext.count("drug") >= 1 :
		response(genericPage)
		error = 0
	else:
		error = 1
		print("an error occured, please try again")	
while True:		
	genericDrug()




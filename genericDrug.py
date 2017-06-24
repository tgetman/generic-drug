#!/usr/bin/python

import wikipedia

brandName = raw_input("Enter brand name of drug: ")

def search (brandName):

	search = wikipedia.search(brandName, results=1)

	genericPage = wikipedia.page(search)

	genericName = genericPage.title
	print(genericName)
	
search(brandName)


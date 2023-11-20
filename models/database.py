#This file contains functions that interact with files in the database

import json

#this function will create a file consisting of a single JSON object at a given path.
#If a file exists there, it will overwrite that file
def createJSONFile(pathname, dictionary):
	#open/create a file for writing at the specified path
	#convert dict to JSON
	#write JSON to file


#this function will create a file consisting of a list of JSON objects at a given path
#if a file exists there, it will overwrite that file
def createJSONListFile(pathname, list_of_dictionaries):
	#open/create a file for writing at the specified path
	#make new list
	#for every dict in given list, add JSON to new list
	#write new list to file


#this function will return a dictionary from a JSON file located at pathname. If the file is not a single
#JSON object, or if the file does not exist, it will throw an error (maybe different errors for each)
def getJSONDict(pathname):
	#checks the validity of the path
	#loads data from file
	#converts to dict
	#returns the dict



#this function will return a list of dictionaries from a JSON list file. If the file is not a list of JSON objects,
#or the file does not exist, it will throw an error.
def getJSONListOfDicts(pathname):
	#check the validity of the pathname
	#load data from the file
	#make a new list, for each JSON in the old list, make a dict in the new list
	#return the list



#this function checks if a provider ID is valid, returning true or false depending 
def checkProviderID(ID):
	#load the provider registry list
	#check each element for a match to the provided ID
	#return true or false 
	pass





#this function checks if a member ID is valid, returning the status of that member if they exist, or "Invalid" if the ID is invalid
def checkMemberID(ID):
	#load the member registry list
	#check each element for a match
	#if one is found, return the status field of that json object, ex. Valid or Suspended or whatever else
	#if no match, return Invalid
	pass





#this function checks if a given service code is valid, returning the true or false depending 
def checkServiceCode(serviceCode):
	#load the provider directory list
	#for each element, check for a match against the given code
	#return true or false to indicate any matches
	pass






#this function adds a member to the member registry file
def addMember():
	#prompt the user for information for the registration
	#call appendToJSONList with that information, adding to the member registration file
	pass



#this function adds a provider to the provider registry file
def addProvider():
	#prompt the user for information for the registration
	#call appendToJSONList with that information, adding to the provider registration file
	pass





#this function deletes a member from the member registration file. It takes a valid member ID, and gives an error if the ID is invalid
def deleteMember(ID):
	#load the member registration file list
	#for each element, check if the ID matches
	#if it does, delete that element from the list
	#give an error if no match
	pass




#this function deletes a provider from the provider registration file. It takes a valid provider ID, and gives an error if the ID in invalid
def deleteProvider(ID):
	#load the provider registry file list
	#for each element, check for matching ID
	#delete the element if it matches
	#give an error if no match
	pass



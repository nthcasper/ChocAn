#This file contains functions that interact with files in the database

import json


#this function takes the keys/values from kwargs and adds them to the json object located at pathname. If no such file exists, it will create the file and add the kwarg elements 
def addJSONToFile(pathname, **kwargs):
	#if the file is empty, create it
	#load the json object from the file into the program
	#update the loaded object with the values from kwargs
	#dump the object to the file
	pass



#this function will add an element to the list of Services provided/received in a provider/member report pointed to by pathname. If no such file exists, it will give an error
def addServiceToReport(pathname, **kwargs):
	#check to make sure the file exists
	#load the report json object
	#create json object from kwarg that represents the service information (different info for provider vs member reports)
	#append that object to the Services list in the report object
	#dump report object to file
	pass



#this function will append a json object, consisting of kwargs, to the list of json objects located at pathname. If no file exists there, throws an error
#for adding service records, adding data to the etf file, 
def appendToJSONList(pathname, **kwargs):
	#check the file exists
	#load the list of objects from the json file
	#create a json object from kwargs
	#append that object to the list
	#dump the list back to the file
	pass



#this function will delete a file, used before running the weekly reports to remove the etf file if one exists, and used when creating a report to remove an old version if it exists
def deleteFile(pathname):
	#delete the file
	pass




#this function checks if a provider ID is valid, returning true or false depending 
def checkProviderID(ID):
	#load the provider registry list
	#check each element for a match to the provided ID
	#return true or false 
	pass




#this function returns the name of a provider, given a valid ID. If the ID is invalid, will give an error
def getProviderName(ID):
	#load the provider registry list
	#check for a match to the given ID
	#return the name field if a match exists
	#give an error if no match is found
	pass


#this function checks if a member ID is valid, returning the status of that member if they exist, or "Invalid" if the ID is invalid
def checkMemberID(ID):
	#load the member registry list
	#check each element for a match
	#if one is found, return the status field of that json object, ex. Valid or Suspended or whatever else
	#if no match, return Invalid
	pass





#this function checks if a given date is valid, returning true or false to indicate. SHOULD THIS BE IN THE DATABASE FILE?? IT DOESNT SEEM TO MATCH, SEEMS MORE LIKE A UTIL FUNCTION
def checkDate(datestring):
	#check the syntax of the date
	pass




#this function checks if a given service code is valid, returning the true or false depending 
def checkServiceCode(serviceCode):
	#load the provider directory list
	#for each element, check for a match against the given code
	#return true or false to indicate any matches
	pass




#this function returns the name of a service, given a valid service code. an invalid code will throw an error
def getServiceName(serviceCode):
	#load the provider directory list
	#for each element, look for a matching service code
	#return the name of the service on finding a match
	#gice an error if no match
	pass





#this function returns the fee of a valid service code, or gives an error if given an invalid code
def getServiceFee(serviceCode):
	#load the provider directory list
	#for each element, look for a matching code
	#return the fee value on a match
	#give an error if no match
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





#this function displays a list of JSON objects stored in a file. Throws an error if the file doesn't exist
#this would be used for displaying all of the registered members/providers, or displaying the provider directory
def displayJSONList(pathname):
	#check the pathname is good
	#load the list stored in the file
	#for each element, print that element
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




#this function checks if a member ID is associated with any service records in the service records file located at pathname, returning true or false depending
def memberReceivedService(ID, pathname):
	#check and load the service records file list
	#loop through all elements, checking for a match
	#return true or false, depending on if any matches were found
	pass



#this function checks if a provider ID is associated with any service records in the service records file located at pathname, returning true or false depending
def providerGaveService(ID, pathname):
	#check and load the service records list that was given
	#loop through all values to look for a match
	#return true or false depending
	pass

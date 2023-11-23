#This file contains functions that interact with files in the database

import json



provDirPath = "../example_database/provider_directory.json"
provRegPath = "../example_database/provider_registry.json"
memRegPath = "../example_database/member_registry.json"
servRecordsPath = "../example_database/service_records/"
reportsPath = "../example_database/reports/"


#this function will create a file consisting of a single JSON object at a given path.
#If a file exists there, it will overwrite that file
def createJSONFile(pathname, dictionary):
	#open/create a file for writing at the specified path
	#convert dict to JSON
	#write JSON to file
	pass


#this function will create a file consisting of a list of JSON objects at a given path
#if a file exists there, it will overwrite that file
def createJSONListFile(pathname, list_of_dictionaries):
	#open/create a file for writing at the specified path
	#make new list
	#for every dict in given list, add JSON to new list
	#write new list to file
	pass


#this function will return a dictionary from a JSON file located at pathname. If the file is not a single
#JSON object, or if the file does not exist, it will throw an error (maybe different errors for each)
def getJSONDict(pathname):
	try:
		with open(pathname, "r") as file:
			dictionary = json.load(file)
			if (type(dictionary) != dict):
				raise ValueError

	except IOError:
		print("ERROR: file not found")
		raise
	except ValueError:
		print("ERROR: file is not a valid .json dictionary")
		raise

	pass



#this function will return a list of dictionaries from a JSON list file. If the file is not a list of JSON objects,
#or the file does not exist, it will throw an error.
def getJSONListOfDicts(pathname):
	try:
		with open(pathname, "r") as file:
			listOfDicts = json.load(file)
			if (type(listOfDicts) != list):
				raise ValueError

	except IOError:
		print("ERROR: file not found")
		raise
	except ValueError:
		print("ERROR: file is not a valid .json list")
		raise




#this function checks if a provider ID is valid, returning true or false depending 
def checkProviderID(ID):
	with open(provRegPath, "r") as file:
		providerList = json.load(file)
		file.close()
		for provider in providerList:
			if int(provider['ID']) == int(ID): 
				return True
		return False




#this function checks if a member ID is valid, returning the status of that member if they exist, or "Invalid" if the ID is invalid
def checkMemberID(ID):
	with open(memRegPath, "r") as file:
		memberList = json.load(file)
		file.close()
		for member in memberList:
			if int(member['ID']) == int(ID):
				return member['status']
		return "Invalid"		





#this function checks if a given service code is valid, returning the true or false depending 
def checkServiceCode(serviceCode):
	with open(provDirPath, "r") as file:
		provDir = json.load(file)
		file.close()
		for service in provDir:
			if int(service['code']) == int(serviceCode):
				return True
		return False




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



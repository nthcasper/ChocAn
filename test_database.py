from database import *
import pytest
import os

def test_create_new_json_file():
	path = "test1.json"
	data = {
		'name': "simon",
		'status': "amazing",
		'age': 99
	}

	assert not os.path.isfile(path)
	
	createJSONFile(path, data)
	assert os.path.isfile(path)
	
	with open(path, "r") as file:
		jsonData = json.load(file)	
		file.close()

	assert jsonData['name'] == "simon"
	assert jsonData['status'] == "amazing"
	assert jsonData['age'] == 99

	os.remove(path)


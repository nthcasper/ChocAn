# import models.database as db
from datetime import datetime
from .data import *
from models.database import addProvider


class ManagerControl:
    def __init__(self):
        pass

    def makeDict(self, dataObj):
        dataDict = dict(name=dataObj.name, Id=dataObj.Id, address=dataObj.address,
                        city=dataObj.city, state=dataObj.state, zipcode=dataObj.zipcode)
        return dataDict
    def addProvider(self,providerObj):
        providerDict = self.makeDict(providerObj)
        addProvider(providerDict)

    # this obj will have things like name, number etc..
    def addMember(self,memberObj):
        # call the data base class funtion to do the ading
        return database.add(memberObj)

    def editMember(memberObj):
        return database.update(memberObj, memberId)

    def editProvider(providerObj):
        return database.update(providerObj, providerId)

    def removeProvider():
        pass

    def removeMember():
        pass

    def viewMemberReport(memberFile):
        return database.memberReport(memberId)

    def viewProviderReport(providerFile):
        return database.providerReport(providerId)

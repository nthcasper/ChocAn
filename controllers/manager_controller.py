import models.database as db

class ManagerControl:
    def __init__(self):
        pass

    def addProvider(providerObj):
        return db.addProvider()  # shoudl this need arguments

    # this obj will have things like name, number etc..
    def addMember(memberObj):
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

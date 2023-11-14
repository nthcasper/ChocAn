class manager_control:
    def __init__(self):
        pass

    def login(self, idNumber):
        if (idNumber.isnumeric()):
            if (self.validateManager(idNumber)):
                isManager = True
        else:
            return False

    def validateManager(idNumber):
        # travese through data base
        # if match with idNumber
        # return true
        # otherwise return false
        pass

    # this obj will have things like name, number etc..
    def addMember(memberObj):
        # call the data base class funtion to do the ading
        return database.add(memberObj)

    def updateMember(memberObj):
        return database.update(memberObj, memberId)

    def updateProvider(providerObj):
        return database.update(providerObj, providerId)

    def viewMemberReport(memberFile):
        return database.memberReport(memberId)

    def viewproviderReport(providerFile):
        return database.providerReport(providerId)

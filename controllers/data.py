class BasicData:
    def __init__(self, name, Id, address, city, state, zipcode):
        self.name = name
        self.Id = Id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
    
    def getId():
        while True:
            Id = input("Enter your 9 digit id: ")
            if not Id.isdigit():
                print("The id should only contain numbers")
            elif len(Id != 9):
                print("The Id must have exactly 9 numbers")
            else:
                return int(Id)

    def getZipcode():
        while True:
            Zipcode = input("Enter your Zipcode: ")
            if not Zipcode.isdigit():
                print("The Zipcode should only contain numbers")
            elif len(Zipcode != 5):
                print("The Zipcode must have exactly 5 numbers")
            else:
                return int(Zipcode) 
    
    def createBasicData(self):
        name = input("Enter your name: ")
        Id = self.getId()
        address = input("Enter your address: ")
        city = input ("Enter your city: ")
        state = input("Enter your state: ")
        zipcode = self.getZipcode()
        return BasicData(name, Id, address, city, state, zipcode)

class ServiceData:
    def __init__(self, time, dateOfService, providerNumber, memberNumber, serviceCode, comments) -> None:
        self.time = time
        self.dateOfService = dateOfService
        self.providerNumber = providerNumber
        self.memberNumber = memberNumber
        self.serviceCode = serviceCode
        self.comments = comments
        pass

    def getProviderNumber():
        while True:
            providerNumber = (input("Enter the provider number: "))
            if not providerNumber.isdigit():
                print("The provider Number should only contain numbers")
            elif len(providerNumber != 9):
                print("The provider number must have exaclty 9 numbers")
            else:
                return int(providerNumber)

    def getMemberNumber():
        while True:
            memberNumber = (input("Enter the member number: "))
            if not memberNumber.isdigit():
                print("The member Number should only contain numbers")
            elif len(memberNumber != 9):
                print("The member number must have exaclty 9 numbers")
            else:
                return int(memberNumber)

    def getServiceCode():
        while True:
            serviceCode = (input("Enter the service code: "))
            if not serviceCode.isdigit():
                print("The service code should only contain numbers")
            elif len(serviceCode != 6):
                print("The service code must have exaclty 9 numbers")
            else:
                return int(serviceCode)

    def createServiceData(self):
        time = datetime.datetime.now()
        dateOfService = input("date: ")
        providerNumber = self.getProviderNumber()
        memberNumber = self.getMemberNumber()
        serviceCode = self.getServiceCode()
        comments = input("Comments: ")
        return ServiceData(time, dateOfService, providerNumber, memberNumber, serviceCode, comments)

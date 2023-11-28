import provider_controller as pc


'''Displays the main menu'''
def main_menu():
    print("1. Create Service Record")
    print("2. Show Provider Directory")
    print("3. Logout")

'''Displays provider directory. Must be callable anywhere????'''
def displayProviderDirectory():
    directory = pc.ProviderControl.getProviderDirectory()

    print(directory)

'''This will take user input and pass it to provider.py'''
def createServiceRecord():
    '''
    memberid = input()
    if checkmemberid(memberid) == False:
        return False
    
    userDict = {
        time = datetime.datetime.now()
        dateOfService = input("date: ")
        providerNumber = input("provider number: ")
        memberNumber = input("member number: ")
        serviceCode = input("code: ")
        comments = input("comments: ")
    }

    fee = createRecord(userDict)
    if fee == 0:
        return False

    userDict = {
        time = datetime.datetime.now()
        dateOfService = input("date: ")
        providerNumber = input("provider number: ")
        memberNumber = input("member number: ")
        serviceCode = input("code: ")
        comments = input("comments: ")
    }

    return verifyAllData(userDict)
    '''


'''Placeholder for provider.py function'''
def login(providerID):
    pass


if __name__ == '__main__':
    while (login(input("Please enter your Provider ID: "))):
        print("Invalid Provider ID.")

    main_menu()
    choice = int(input("Please enter choice: "))
    while choice != 3:
        if choice == 1:
            createServiceRecord()
        elif choice == 2:
            displayProviderDirectory()
        else:
            print("Invalid Choice.")

        main_menu()
        choice = int(input("Please enter choice: "))

    print("Logging out")

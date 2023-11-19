#import provider.py
#import database.py #To gain direct access to some display functions?

'''Displays the main menu'''
def main_menu():
    print("1. Create Service Record")
    print("2. Show Provider Directory")
    print("3. Logout")

'''Displays provider directory. Must be callable anywhere????'''
def displayProviderDirectory():
    #Should this file have access to database.py?
    #Should this function be called by keyboard interrupt, haha.
    print("Provider Directory!")

'''This will take user input and pass it to provider.py'''
def createServiceRecord():
    #Should I call provider.py twice? Once for entering data, second for verification?
    time = datetime.datetime.now()
    dateOfService = input("date: ")
    providerNumber = input("provider number: ")
    memberNumber = input("member number: ")
    serviceCode = input("code: ")
    comments = input("comments: ")

    return updateFunction(time.strftime("%m-%d-%Y %H:%M:%S"),
                        dateOfService, providerNumber, memberNumber, serviceCode, comments)

'''Placeholder for provider.py function'''
def login(providerID):
    pass


if __name__ == '__main__':
    '''Does not allow the user to move on until a valid id is given.'''
    while (login(input("Please enter your Provider ID: "))):
        #Should this be an if or a while?
        #An if would quit on fail. 
        #A while would continue until success.
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
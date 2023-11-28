
import __init__
import manager_controller as mc
import data

'''Displays the user options'''


def main_menu():
    print("1. End of Week")
    print("2. Generate ETF Report")
    print("3. Generate Provider Reports")
    print("4. Generate Member Reports")
    print("5. Update Member Registry")
    print("6. Update Provider Registry")
    print("7. Turn Off Terminal")


'''Calls the following three functions.'''


def endOfWeek():
    # Should this call an endOfWeek function or just call each report function?
    # Depends on how the manager.py team wants to do.
    pass


'''Placeholder for manager.py function'''


def etfReport():
    pass


'''Takes in a member id. Calls manager.py function'''


def memberReport():
    pass


'''Takes in a provider id. Calls manager.py function'''


def providerReport():
    pass


'''Take member info and call manager.py function.'''


def updateMembers():
    # Should this be split up into three functions, or let manager.py figure it out?
    # Example: the user could enter an existing member id along with data to be changed.
    # Example: the user could enter a new member id along with data to be added.
    # Example: the user could enter an existed member id and empty data to delete member.
    # --Places more effort on manager.py team.--

    name = input("name: ")
    ID = input("name: ")
    address = input("name: ")
    city = input("name: ")
    state = input("name: ")
    zipcode = input("name: ")

    # return memberUpdate(name, number, address, city, state, zipcode)


'''Take provider info and call manager.py function.'''


def updateProviders():
    # Should this be split up into three functions, or let manager.py figure it out?

    name = input("name: ")
    number = input("name: ")
    address = input("name: ")
    city = input("name: ")
    state = input("name: ")
    zipcode = input("name: ")

    # return providerUpdate(name, number, address, city, state, zipcode)


# if __name__ == '__main__':
#     main_menu()
#     choice = int(input("Please enter choice: "))
#     while choice != 7:
#         if choice == 1:
#             endOfWeek()
#         elif choice == 2:
#             etfReport()
#         elif choice == 3:
#             memberReport()
#         elif choice == 4:
#             providerReport()
#         elif choice == 5:
#             updateMembers
#         elif choice == 6:
#             updateProviders()
#         else:
#             print("Invalid Choice.")

#         main_menu()
#         choice = int(input("Please enter choice: "))

#     print("Shutting of terminal.")

info = data.BasicData()
manager = mc.ManagerControl()
myData = info.createBasicData()
manager.addProvider(myData)

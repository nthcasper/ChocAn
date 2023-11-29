import provider_controller as pc
import data


'''Displays the main menu'''
def main_menu():
    print("1. Create Service Record")
    print("2. Show Provider Directory")
    print("3. Logout")


'''Displays provider directory. Must be callable anywhere????'''
def displayProviderDirectory():
    directory = pc.ProviderControl().getProviderDirectory()

    print(directory)


'''This will take user input and pass it to provider.py'''
def createServiceRecord(providerNumber):
    memberRecord = data.ServiceData()
    memberRecord.memberNumber = memberRecord.getMemberNumber()
    memberStatus = pc.ProviderControl().messageMemberId(memberRecord.memberNumber)
    if (memberStatus != "Valid"):
        print(memberStatus)
        return
    
    print("Validated")
    memberRecord.time = memberRecord.getDateOfService()
    memberRecord.serviceCode = memberRecord.getServiceCode()
    #
    #
    #
    #NEED A FUNCTION THAT VERIFIES THE SERVICE!!!!!
    #
    #
    #
    memberRecord.comments = memberRecord.getComment()

    pc.ProviderControl().createServiceRecord(
            providerNumber,
            memberRecord.memberNumber, 
            memberRecord.serviceCode,
            memberRecord.dateOfService,
            memberRecord.comments)
    
    print(f"Fee for the service is: {pc.ProviderControl().getServiceFee(memberRecord.serviceCode)}")
    serviceFee = input("Verify the service fee: ")
    while(pc.ProviderControl().verifyServiceFee(serviceFee, memberRecord.serviceCode) == False):
        print(f"Fee for the service is: {pc.ProviderControl().getServiceFee(memberRecord.serviceCode)}")
        serviceFee = input("Verify the service fee: ")

    #
    #
    #
    #NEED A FUNCTION THAT VERIFIES MEMBER RECORD AND FEE
    #
    #
    #


'''Placeholder for provider.py function'''
def login():
    providerNumber = data.ServiceData().getProviderNumber()

    while (pc.ProviderControl().giveAuthorization(providerNumber) == False):
        providerNumber = data.ServiceData().getProviderNumber()

    return providerNumber


if __name__ == '__main__':
    providerNumber = login()

    choice = 0
    while choice != 3:
        try:
            main_menu()
            choice = int(input("Please enter choice: "))

            if choice == 1:
                createServiceRecord(providerNumber)
            elif choice == 2:
                displayProviderDirectory()
            elif choice == 3:
                pass
            else:
                print("Invalid Choice.")

        except ValueError:
            print("Invalid Choice.")

    print("Logging out.")

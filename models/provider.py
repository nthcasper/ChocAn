# Provider Model

# Authorization Function
"""
This will be a boolean function. Checks the ID of the provider. If the provider ID is correct. 
Returns a true statement. 
def give_Auth(int provider_ID):
    if checkProvderID function is True
        don't say anything bc the provider was able to log in
    else
        print('You have entered a invalid ID. Try again.')
        return false.
        the authorize function from the view can use this as a way to tell the provider to 
        log in again if they entered it in wrong.
"""

# Member Valid. Member Invalid.
"""
For the valid and invalid functions, it would call the check member_ID function to see if it
returned a true statement or not and send a message accordingly.

def message_ID(int memberID):
    if checkMemberID is True
        if memberRecievedService is True
            If they did pay their service
            print("Validated")
            else
                print("Suspended")
    else
        print("Invalidated")
"""

# Message Fee
"""
Will use the getServiceFee function and return the fee from that function
def message_Fee(int serviceCode)
    if getServiceFee is True
        return the fee

    else
        print("Enter the code again")
"""


# Provider Directory
"""
Check the function that asks for accessing the directory. If that function returns a true
statement. Then this function will display a JSON file. Maybe?
"""

import models.database as db  # im not sure how we are going to change this yet
# from models import database as db #im not sure how we are going to change this yet
import datetime


class ProviderControl:
    def __init__(self):
        # Initialize with file paths for the provider directory and service records
        # might need to move this around depending on how were are keeping the files, like in folders or not
        self.provider_directory = 'example_database\\provider_directory.json'
        # self.service_records_file = 'example_database\\week_1-1_records.json' #might need to move this around depending on how were are keeping the files, like in folders or not

    def giveAuthorization(self, providerId):
        """
        Verifies the provider ID.
        Checks if the provider ID is exactly 9 digits.
        Returns True if valid, False otherwise.
        """
        if len(providerId) != 9 or not providerId.isdigit():
            return False
        return db.checkProviderID(providerId)

    def messageMemberId(self, memberId):
        """
        Check the status of member ID and returns a status message.
        Possible return statuses are "Valid", "Invalid", and "Suspended".
        """
        if len(memberId) != 9 or not memberId.isdigit():
            return "Invalid"  # Member ID must be a 9-digit number

        memberStatus = db.checkMemberID(memberId)
        if memberStatus:
            return memberStatus  # actual status returned from the database
        else:
            return "Invalid"  # if the database check does not return a status, assume "Invalid"

    def logout(self):
        """
        Resets the provider ID, effectively logging out the provider.
        Returns -1 to indicate the provider is logged out.
        """
        return -1

    def getProviderDirectory(self):
        """
        Retrieves the provider directory from a JSON file.
        Returns a list of service details.
        """
        return db.getJSONListOfDicts(self.provider_directory)

    def verifyServiceFee(self, serviceFee, serviceCode):
        """
        Verifies if the provided service fee matches the service code.
        Returns True if the fee is correct, False otherwise.
        """
        if not db.checkServiceCode(serviceCode):
            return False

        provider_directory = db.getJSONListOfDicts(self.provider_directory)
        for service in provider_directory:
            if service['code'] == serviceCode and str(service['fee']) == serviceFee:
                return True
        return False

    def createServiceRecord(self, providerId, memberId, serviceCode, dateOfService, comments):
        """
        Creates a service record object with the provided details.
        The function then returns this object so it can be appended to the service records file by the terminal.
        """
        if self.giveAuthorization(providerId) and self.messageMemberId(memberId) == "Valid":
            serviceFee = self.getServiceFee(serviceCode)
            if serviceFee and self.verifyServiceFee(serviceFee, serviceCode):
                current_datetime = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                current_date, current_time = current_datetime.split(' ')
                service_record = {
                    "current": {
                        "date": current_date,
                        "time": current_time
                    },
                    "date": dateOfService,
                    "provider_ID": providerId,
                    "member_ID": memberId,
                    "service_code": serviceCode,
                    "comments": comments
                }
                # Return the service record object to the terminal/caller
                return service_record
            else:
                return None, "Service fee verification failed."
        else:
            return None, "Provider or Member ID is invalid."

    def getServiceFee(self, serviceCode):
        """
        Retrieves the service fee for a given service code from the provider directory.
        Returns the service fee if found, None otherwise.
        """
        provider_directory = self.getProviderDirectory()
        for service in provider_directory:
            if service['code'] == serviceCode:
                return service['fee']
        return None

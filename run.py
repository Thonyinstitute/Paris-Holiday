# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file", 
    "https://www.googleapis.com/auth/drive"
]



def get_holiday_document():
    """
    Get required documents from the traveller to achive Paris holiday
    """
    while True:
        print("Have your passport, Ticket and hotel reservation")
        print("You are required to have all three documents to travel to Paris")
        
        data_str = input("Submit your documents here:")

        holiday_document = document_str.split(",")

        if validate_document(holiday_document):
            print("Documents are Valid")
            break
        
        return holiday_document


print("Paris Holiday")
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials

"""
Google API calling, the url and the attributes
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file", 
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('paris_holiday')

expense = SHEET.worksheet('expense')
data = expense.get_all_values()

"""
Google API Verification and figlet print out
"""
print(pyfiglet.figlet_format('Welcome to Paris'))
print(data)





def get_doc_data():
    """
    Ask user for travel documents
    """

    print("Submit traveling document")
    print("Documents should be three")
    print("documents type are, Passport, Ticket and Cash")
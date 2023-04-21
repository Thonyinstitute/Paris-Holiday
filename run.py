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

"""
Google API Verification and figlet print out
"""
print(pyfiglet.figlet_format('Welcome to Paris'))

def get_expense_data():
    """
    Requesting expense from user
    """
    print("Please enter travelling documents.")
    print("Documents must be three type only.")
    print("Documents Type are: Passport, Ticket and Cash.")

    data_str = input("Enter your documents here: ")
    print(f"The documents provided are {data_str}")

get_expense_data()





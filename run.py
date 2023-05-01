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
print(data)


print(pyfiglet.figlet_format('Welcome to Paris'))


def get_expense_data():
    while True:
        print("Please enter tarvel data")
        print("Data should be five values, separated by comma")
        print("Example are: 1,2,3,4,5")


        data_str = input("Please enter data here: ")
        print(f"Data provided are {data_str}")

        expense_data = data_str.split(",")
        

        if validate_data(expense_data):
            print("Data are valid")
            break
            
    return expense_data

def validate_data(values):
    print(values)
    """
    
    """
    try:
        [int(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False
    return True


def update_expense_worksheet(data):
    """
    
    """
    print("Updated expense worksheet.....\n")
    expense_worksheet = SHEET.worksheet('expense')
    expense_worksheet.append_row(data)
    print("Expense worksheet updated successfully")


data = get_expense_data()
expense_data = [int(num) for num in data]
update_expense_worksheet(expense_data)



      


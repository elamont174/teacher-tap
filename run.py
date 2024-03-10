import gspread
from google.oauth2.service_account import Credentials

#scope taken from Code Institute Love Sandwiches project

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('teacher-tap')

def get_exam_data():
    """
    Get exam result data from user
    """
    while True:
        print("Please enter exam result and predicted grade for each student.")
        print("Data should be in the format 'Student Name, Predicted Grade, Exam Mark'.")
        print("Example: Joe Bloggs, 7, 54\n")

        data_str = input("Enter your data here: ")
        
        exam_data = data_str.split(",")
        validate_data(exam_data)

        if validate_data(exam_data):
            print("Data is valid")
            break 

    return exam_data

data = get_exam_data()

def validate_data(values):
    """
    Ensures 'Student Name' has first and surname; Predicted Grade is between 1-9 as an integer; Exam mark is between 0-100 as an integer. Ensures three values added. 
    Raises error if does not fit this format.
    """
    # How to validate a string and 2 integers in one list? 
    try:
        if len(values) != 3:
            raise ValueError(f"3 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True   

get_exam_data()
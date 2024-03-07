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
    print("Please enter exam result and predicted grade for each student.")
    print("Data should be in the format 'Student Name, Predicted Grade, Exam Mark'.")
    print("Example: Joe Bloggs, 7, 54\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_exam_data()
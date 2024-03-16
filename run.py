import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from tabulate import tabulate


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
    Get exam result data from user.
    Run a while loop to collect a valid string of data from the user via the terminal. Loop will continually request data until it is valid.
    """
    while True:
        print("Please enter predicted grade and exam score for each student.")
        print("Data should be in the format 'Student Name, Predicted Grade, Exam Score'.")
        print("Example: Joe Bloggs, 7, 54\n")

        data_str = input("Enter your data here: ")
        
        exam_data = data_str.split(",")

        if validate_data(exam_data):
            print("Data is valid")
            break 

    return exam_data

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

data = get_exam_data()

def calculate_exam_grade():
    """
    Calculates the exam grade from the exam mark
    """
    print("Calculating exam grade...\n")
    #datasheet = SHEET.worksheet("datasheet").get_all_values()
    exam_score = int(data[2])

    if exam_score >= 80:
        exam_grade = 9
    if exam_score >= 70:
        exam_grade = 8
    if exam_score >= 60:
        exam_grade = 7
    if exam_score >= 50:
        exam_grade = 6
    if exam_score >= 40:
        exam_grade = 5
    if exam_score >= 30:
        exam_grade = 4
    if exam_score < 40:
        exam_grade = 3
        print(U)
    
    return int(exam_grade)

predicted_grade = int(data[1])
exam_grade = calculate_exam_grade()

def calculate_on_target():
      if exam_grade > predicted_grade:
        on_target = "Above"
      if exam_grade == predicted_grade:
        on_target = "On"
      if exam_grade < predicted_grade:
        on_target = "Below"

      return on_target

on_target = calculate_on_target()

def generate_intervention_strategy():
         if on_target == "Above":
             intervention_strategy == "Positive email"
         if calculate_on_target == "On":
             intervention_strategy == "Verbal praise"
         if calculate_on_target == "Below":
             intervention_strategy == "Parental phonecall"

intervention_strategy = generate_intervention_strategy()

def update_data_worksheet(data):
    """
    Update exam data worksheet
    """
    print("Updating exam worksheet...\n")
    exam_grade = calculate_exam_grade()
    data.append(exam_grade)
    on_target = calculate_on_target()
    data.append(on_target)
    intervention_strategy = generate_intervention_strategy()
    data.append(intervention_strategy)
    exam_worksheet = SHEET.worksheet("datasheet")
    exam_worksheet.append_row(data)
    print("Exam data worksheet updated successfully")

def update_positive_email_worksheet(data):
    """
    Updates the postive email worksheet
    """
    if data[5] == "Positive email":
        exam_worksheet = SHEET.worksheet("positive-email")
        name = data[0]
        exam_worksheet.append_row(name,f"Well done to {name} for achieving {exam_score} marks in their recent Science exam! This is a grade {exam_grade} which is above their predicted target! Congratulations!")
        print("Positive email worksheet updated successfully")

def main():
    """
    Run all program functions
    """
    data = get_exam_data()
    exam_data = [x for x in data]
    update_data_worksheet(exam_data)

print("Welcome to Teacher Tap!")
main()
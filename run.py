import gspread
from google.oauth2.service_account import Credentials


""" Scope taken from Code Institue Love Sandwiches project. """
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('teacher-tap')


def get_name_list():
    """ Get exam result data from user: student name.
    Run a while loop to collect valid data from the user via the terminal.
    Loop will continually request data until it is valid.
    """
    print(f"""Please enter student's first and surname:""")
    name_str = False
    while name_str == False:
        name_str = input("Enter name here:\n").strip()
        try:
            name_list = name_str.split(" ")
            if len(name_list) == 2:
                if len(name_list[0]) > 1 and len(name_list[1]) > 1:
                    print("Data is valid\n")
                    name_str == True
                elif len(name_list[0]) <= 1:
                    print("first name should be more than 1 letter")
                    name_str = False
                elif len(name_list[1]) <= 1:
                    print("last name should be more than 1 letter")
                    name_str = False
            else:
                print(f"""
Invalid data: ensure you enter a first name and surname, separated by a space\n""")
                name_str = False
        except ValueError as e:
            print(f"Invalid data: {e}, ensure you enter a first name and surname, separated by a space\n")
    return name_str


def get_predicted_grade():
    """ Get exam result data from user: predicted grade.
    Run a while loop to collect valid data from the user via the terminal.
    Loop will continually request data until it is valid.
    """
    print(f"""Please enter student's predicted grade""")
    predicted_grade1 = False
    while predicted_grade1 == False:
        predicted_grade1 = input("Student's predicted grade:\n").strip()
        try:
            if predicted_grade1.isdigit() and int(predicted_grade1) >= 1 and int(predicted_grade1) <= 9 and len(predicted_grade1) == 1: 
                print("Data is valid\n")
                predicted_grade1 == True
            else:
                print(f"""
Invalid data: enter an integer between 1-9\n""")
                predicted_grade1 = False
        except ValueError as e:
            print(f"Invalid data: enter an integer between 1-9\n")
    return predicted_grade1


def get_exam_score():
    """ Get exam result data from user.
    Run a while loop to collect valid data from the user via the terminal. 
    Loop will continually request data until it is valid.
    """
    print(f"""Please enter student's exam score.""")
    exam_score1 = False
    while exam_score1 == False:
        exam_score1 = input("Student's exam score:\n").strip()
        try:
            if exam_score1.isdigit() and int(exam_score1) >= 0 and int(exam_score1) <= 100 and len(exam_score1) <= 3 and len(exam_score1) >= 1:
                    print("Data is valid\n")
                    exam_score1 == True
            else:
                print(f"""
Invalid data: enter an integer between 0-100\n""")
                exam_score1 = False
        except ValueError as e:
            print(f"Invalid data: enter an integer between 0-100\n")
    return exam_score1


def calculate_exam_grade(exam_score):
    """Calculates the exam grade from the exam mark."""
    print("Calculating exam grade...\n")
    if exam_score < 30:
        exam_grade = 3
    if exam_score >= 30:
        exam_grade = 4
    if exam_score >= 40:
        exam_grade = 5
    if exam_score >= 50:
        exam_grade = 6
    if exam_score >= 60:
        exam_grade = 7
    if exam_score >= 70:
        exam_grade = 8
    if exam_score >= 80:
        exam_grade = 9
    return int(exam_grade)


def calculate_on_target(exam_grade, predicted_grade):
    """Compares the students exam grade with their predicted grade.
    Calculates whether the student is on/above/below target
    """
    if exam_grade > predicted_grade:
        on_target = "Above"
    if exam_grade == predicted_grade:
        on_target = "On"
    if exam_grade < predicted_grade:
        on_target = "Below"
    return on_target


def generate_intervention_strategy(on_target):
    """ Generates intervention strategy based on whether student is on target."""
    intervention_strategy = ""
    if on_target == "Above":
        intervention_strategy = "Positive email"
    if on_target == "On":
        intervention_strategy = "Verbal praise"
    if on_target == "Below":
        intervention_strategy = "Parental phonecall"
    return intervention_strategy


def update_data_worksheet(data):
    """Updates exam data worksheet."""
    print("Updating exam worksheet...\n")
    exam_worksheet = SHEET.worksheet("datasheet")
    exam_worksheet.append_row(data)
    print("Exam data worksheet updated successfully")


def  update_positive_email_worksheet(name_str, exam_score, exam_grade, intervention_strategy):
    """ Updates the positive email worksheet if intervention strategy is 'Positive email' """
    if intervention_strategy == "Positive email":
        email_worksheet = SHEET.worksheet("positive-email")
        name = str.split(name_str)
        fname = name[0]
        positive_data = [(name_str), (f"""Well done to {fname} for achieving {exam_score} marks in their recent Science exam! This is a grade {exam_grade} which is above their predicted target! Congratulations!""")]
        email_worksheet.append_row(positive_data)
        print("Positive email worksheet updated successfully")


def update_parental_phonecall_worksheet(name_str, intervention_strategy):
    """ Updates the parental phonecall worksheet if intervention strategy is 'Parental phonecall' """
    if intervention_strategy == "Parental phonecall":
        call_worksheet = SHEET.worksheet("parent-call")
        call_name = [(name_str)]
        call_worksheet.append_row(call_name)
        print("Parental call worksheet updated successfully")


def main():
    """ Run all program functions. """
    print("Welcome to Teacher Tap!")
    name_str = get_name_list()
    predicted_grade = get_predicted_grade()
    exam_score = int(get_exam_score())
    exam_grade = calculate_exam_grade(exam_score)
    on_target = calculate_on_target(exam_grade, int(predicted_grade))
    intervention_strategy = generate_intervention_strategy(on_target)
    data = [(name_str), (int(predicted_grade)), (int(exam_score)), 
    (int(exam_grade)), (on_target), (intervention_strategy)]
    update_data_worksheet(data)
    update_positive_email_worksheet(name_str, exam_score, exam_grade, intervention_strategy)
    update_parental_phonecall_worksheet(name_str, intervention_strategy)


if __name__ == "__main__":
    main()
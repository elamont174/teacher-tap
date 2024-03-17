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


#Enter name (First and Surname)
#Enter student's predicted grade (must be an integer 1-9)
#Enter student's exam score (must be an integer 1-100)
def get_exam_data():

    """ Get exam result data from user.Run a while loop to collect valid 
    data from the user via the terminal. Loop will continually 
    request data until it is valid."""
    

    print(f"""Please enter student's first and surname:""")
    name_str = False
    while name_str == False:
        name_str = input("Enter name here: ").strip()
        try:
            validate_data(exam_data, "name"):
            print("Data is valid")
            name_str = True
        except ValueError as e:
        print(f"Invalid data: {e}, ensure you enter a first name and surname, separated by a space.\n")
        return False

        if validate_data(exam_data):
            print("Data is valid")
            break 

    return name_list

    print(f"""Please enter student's predicted grade:""")
    predicted_grade_raw = False
    while predicted_grade_raw == False:
        predicted_grade_raw = input("Student's predicted grade: ").strip()
        try:
            if int(predicted_grade_raw) >= 1 and <= 9: 
            print("Data is valid")
            predicted_grade_raw = True
        except ValueError as e:
        print(f"Invalid data: {e}, enter an integer between 1-9\n")
        return False

        if validate_data(exam_data):
            print("Data is valid")
            break 

    return predicted_grade

    print(f"""Please enter student's exam score:""")
    exam_score_raw = False
    while exam_score_raw == False:
        exam_score_raw = input("Student's exam score out of 100: ").strip()
        try:
            if int(exam_score_raw) >= 0 and <= 100: 
            print("Data is valid")
            exam_score_raw = True
        except ValueError as e:
        print(f"Invalid data: {e}, enter an integer between 0-100\n")
        return False

        if validate_data(exam_data):
            print("Data is valid")
            break 

    return exam_score


#Validates data as a string with 2 words, an integer between 1-9, an integer 
#between 1-100
def validate_data(values, type):

    """Ensures 'Student Name' has first and surname; 
    Predicted Grade is between 1-9 as an integer; Exam mark is between 0-100 as 
    an integer. Ensures three values added. 
    Raises error if does not fit this format."""


    if type == "name":
        try:
            name_list = values.split(" ")
            # ["jsdfs", "sdfsdf"]
            if len(name_list) == 2:
                # proceede
                pass
            else:
                # raise
                break
    try:
        if len(values) != 3:
            raise ValueError(f"3 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True   


#Takes exam score and converts to an grade (integers)
def calculate_exam_grade(some_data):

    """Calculates the exam grade from the exam mark"""


    print("Calculating exam grade...\n")
    exam_score = int(some_data[2])

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


#Takes exam grade, compares to predicted grade and 
#calculates whether student is on/above/below target
def calculate_on_target():

    """Compares the students exam grade with their predicted grade and 
    calculates whether the student is on/above/below target"""


    if exam_grade > predicted_grade:
        on_target = "Above"
    if exam_grade == predicted_grade:
        on_target = "On"
    if exam_grade < predicted_grade:
        on_target = "Below"

    return on_target


#Takes on/above/below target and generates an intervention strategy
def generate_intervention_strategy():

    """ Generates intervention strategy based on whether student is 
    on/above/below target from a pre-determined list"""


    intervention_strategy = ""
    if on_target == "Above":
        intervention_strategy = "Positive email"
    if calculate_on_target == "On":
        intervention_strategy = "Verbal praise"
    if calculate_on_target == "Below":
        intervention_strategy = "Parental phonecall"

    return intervention_strategy


def update_data_worksheet():
#Concatenates "Name, Predicted Grade, Exam score, Exam grade, Target, 
#Intervention strategy" into a list (using append)
#Adds list to spreadsheet
def update_data_worksheet(data):

    """ Concatenates entered and calculateddata into a list and updates 
    exam data worksheet """


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


#If intervention strategy is "Positive email", adds name and message to 
#separate tab of worksheet
def update_positive_email_worksheet(data):
    """
    Updates the postive email worksheet
    """
    if data[5] == "Positive email":
        exam_worksheet = SHEET.worksheet("positive-email")
        name = data[0]
        exam_worksheet.append_row(
            name,
            f"""Well done to {name} for achieving {exam_score} marks in their recent Science exam! This is a grade {exam_grade} which is above their predicted target! Congratulations!"""
        )
        print("Positive email worksheet updated successfully")


def update_parental_phonecall_worksheet():
#If intervention strategy is "Parental phonecall", adds name to separate tab of 
#worksheet


def main():
    
    """ Run all program functions """


    print("Welcome to Teacher Tap!")
    data = get_exam_data()
    validate_data()
    calculate_exam_grade(data)
    exam_grade = calculate_exam_grade()
    calculate_on_target(exam_grade)
    on_target = calculate_on_target()
    generate_intervention_strategy(on_target)
    intervention_strategy = generate_intervention_strategy()
    update_data_worksheet()
    update_positive_email_worksheet()
    update_parental_phonecall_worksheet()
    exam_data = [x for x in data]
    update_data_worksheet(exam_data)

if __name__ == "__main__":
    main()
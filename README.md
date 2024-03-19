# Teacher Tap
- Deployed link: [Teacher Tap](https://teacher-tap-0d3c391f8f6b.herokuapp.com/)
- [Screenshot of the running program "Teacher Tap"](assets/images/teacher-tap.png)
- Teacher Tap is designed for Secondary school teachers to input student data after sitting an exam. The user is prompted to input the student's name, predicted grade and exam score. The program will then calculate the grade the student got for the exam, whether the student is on target or not and will also generate an intervention strategy for the student. 
- If the student requires an email home, the programme will automatically generate a message that the teacher can copy and paste without having to type it out themselves. If students require a phonecall home, the programme will add their name to a list that the teacher can check off once they have made the relevant phonecalls.
- The concept is that the teacher has marked a set of exam papers and needs to know the exam grades the students get. If the students exam grade is above their predicted grade, their intervention strategy would be a Positive Email home. If the students exam grade is below their predicted grade, their intervention strategy would be a Parental Phonecall home. If the students exam grade is the same as their predicted grade, their intervention strategy would be Verbal Praise. The program would work this out for the teacher and collate all of the relevant information onto a spreadsheet. This would reduce their workload.

## User Stories
- As a first time user, I want the input system to be simple and easy to follow.
- As a first time user, I want to be corrected and given feedback if I make a mistake, as it is an unfamiliar system.
- As a continued user, I want to reduce my workload and only need to enter a few values. 
- As a continued user, I want to display my students details on a spreadsheet.
- As a continued user, I want to have a quick method of working out intervention methods to help my students. 

## Features
- When the program runs, the user is greeted and invited to enter a student's name. If they do not enter a first and surname, separated by a space, which contains at least one letter, they will get an error message and be invited to re-enter the data.
[Screenshot of name entry and validation screen](assets/images/name-validation.png)
- When the correct data has been entered, the user will then be invited to enter the student's predicted grade. If the user did not enter an integer between 1-9, they will get an error message and be invited to re-enter the data.
[Screenshot of predicted grade entry and validation screen](assets/images/predicted-validation.png)
- When the correct data has been entered, the user will then be invited to enter the student's exam score. If the user did not enter an integer between 0-100, they will get an error message and be invited to re-enter the data.
[Screenshot of exam score entry and validation screen](assets/images/score_validation.png)
- Once the teacher has entered all of the data, the program will populate the spreadsheet with the entered data, the exam grade, whether the student is on target and their intervention strategy.
[Screenshot of spreadsheet: datasheet](assets/images/datasheet.png)
- A separate worksheet will also be populated with a message to be emailed to the parents of students who are above target.
[Screenshot of spreadsheet: positive-email](assets/images/positive-email.png)
- Another worksheet will be populated with a list of students who the teacher needs to call home for.
[Screenshot of spreadsheet: parent-call](assets/images/parent-call.png)

## Flowcharts
### Initial planning flowchart
[Original planning flowchart which I created before started the project](assets/images/initial-flowchart.png)
### Updated flowchart 
[Flowchart created once project had been started](assets/images/updated-flowchart.png)

## Technologies used
### Languages
- [Python](https://www.python.org/doc/essays/blurb/)

### Library imports
- gspread 
- google.oauth2.service_account

### Other tools
- [Google sheets](https://www.google.co.uk/sheets/about/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/)

## Bugs
- Initially, I planned a very complicated method of putting data into the spreadsheet, taking data back out of the spreadsheet for calculations then putting data back into the spreadsheet. I then realised that it would be much simpler to just do the calculations and then add all of the data to the spreadsheet at once. This meant that I had to completely restructure the order of the functions that I had written to get the appropriate results. 
- Once the program was working, a bug that required fixing was validation. No matter what the user typed, the program was proceeding as though the data was correct. I used Python Tutor to visualise the code and rewrote the relevant section of the while loop to fix this bug.

## Testing
- I constantly tested the program during the development process to ensure it was running.
- I used [PEP8 Python Checker](https://www.pythonchecker.com/) to check my code. It came back with 68% - Good. [Screenshot of PEP8 score](assets/images/pep8.png)

## Deployment
- Program was deployed to [Heroku](https://www.heroku.com/).
- The deployed link can be found [here](https://teacher-tap-0d3c391f8f6b.herokuapp.com/).

1. In the workspace (in this case created on GitPod), the command "pip3 freeze > requirements.txt" is put into the terminal. This creates a list of requirements that the project needs to run in the 'requirements.txt' file.
2. A [Heroku](https://www.heroku.com/) account needs to be created.
3. Once a Heroku account has been made, navigate to the Dashboard and click "Create New App" (the "New" tab may need to be clicked first and  "Create New App" selected from the dropdown menu).
4. Create a unique name for the app and select the appropriate region.
[Screenshot of 'App name' and 'Choose a region' fields](assets/images/deploy1.png)
5. The following page will contain a navigation bar. Click on 'Settings'.
[Screenshot of navigation bar](assets/images/deploy2.png)
6. Scroll down to 'Config Vars'. Click 'Reveal Config Vars'.
[Screenshot of Config Vars area](assets/images/deploy3.png) 
7. In the box labelled "KEY", type "CREDS". From the workspace, open the "creds.json" file and copy the entire contents. Paste the contents of the "creds.json" file into the box labelled "VALUE". Click "Add". 
8. Add another Config Var with KEY = PORT and VALUE = 8000.
9. Scroll down further to 'Buildpacks'. Click 'Add Buildpack'.
[Screenshot of Buildpacks area](assets/images/deploy4.png)
10. Click the python buildpack and the click 'Add buildpack'. Click the nodejs buildpack and the click 'Add buildpack'.
11. Ensure that the buildpacks are in the correct order: Python first then Node.js. You can drag them if they are in the wrong order.
12. Scroll back to the navigation bar at the top of the page. Click Deploy.
[Screenshot of navigation bar](assets/images/deploy2.png)
13. Next to 'Deployment method', select 'GitHub'. Connect to the appropriate repro on GitHub by typing in the name. Click 'search'. Click 'connect'.
[Screenshot of Deployment method area](assets/images/deploy5.png)
14. Scroll down to 'Automatic deploys'. Select 'Enable Automatic Deploys'. Scroll down to 'Manual deploy'. Click 'Deploy Branch'.
[Screenshot of Deployment method area](assets/images/deploy6.png)
15. Wait for app to be deployed. 

## Future improvements
- Future improvements would include the ability to delete data that had been previously entered or update data if a student resat the exam. 
- There would also be an option to add the class name of the student and have separate worksheets for separate classes.
- Another improvement would be the use of tabulate to extract data from the spreadsheet and display it in the terminal again.  

## Credits

My project was inspired by the [Code Institute](https://codeinstitute.net/)'s Love Sandwiches project from the Full Stack Diploma course. I changed the purpose of the programme, adapted the code and wrote my own functions to make my project unique.

## Acknowledgements

My mentor [Julia Konovalova](https://github.com/IuliiaKonovalova) for her support and assistance. 
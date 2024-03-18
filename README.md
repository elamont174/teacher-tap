# Teacher Tap
Teacher Tap is designed for Secondary school teachers to input student data after sitting an exam. The user is prompted to input the student's name, predicted grade and exam score. The programme will then calculate the grade the student got for the exam, whether the student is on target or not and will also generate an intervention strategy for the student. 
If the student requires an email home, the programme will automatically generate a message that the teacher can copy and paste without having to type it out themselves. If students require a phonecall home, the programme will add their name to a list that the teacher can check off once they have made the relevant phonecalls.

The concept is that the teacher only has to enter a few simple values to the programme and a lot of their workload is then carried out for them. 

## User Stories
- As a first time user, I want the input system to be simple and easy to follow.
- As a first time user, I want to be corrected and given feedback if I make a mistake, as it is an unfamiliar system.
- As a continued user, I want to reduce my workload and only need to enter a few values. 

## Features


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

### Other tools
- [Google sheets](https://www.google.co.uk/sheets/about/)
- [GitHub](https://github.com/)

## Bugs


## Testing


## Deployment

App was deployed to [Heroku](https://www.heroku.com/).

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
Future improvements would include the ability to delete data that had been previously entered or update data if a student resat the exam. 
There would also be an option to add the class name of the student and have separate worksheets for separate classes. 

## Credits

My project was inspired by the [Code Institute](https://codeinstitute.net/)'s Love Sandwiches project from the Full Stack Diploma course. I changed the purpose of the programme, adapted the code and wrote my own functions to make my project unique.

## Acknowledgements

My mentor [Julia Konovalova](https://github.com/IuliiaKonovalova) for her support and assistance. 
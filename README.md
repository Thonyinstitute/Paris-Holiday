![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Paris holiday Application,



The features of the app is to request traveller (user) data and through google API, iterate the data to terminal. The terminal validate the data, check data error and if required update the data. And if the inputted data is valid, the terminal will print successfully. The App logo is styled with pyfiglet welcome to paris

![image](https://user-images.githubusercontent.com/122373462/235650299-b2fdab04-083a-467c-9d3e-43655e3b7179.png)

## Information on how to use the App

* Click to open  
* Please enter travel data
* Data should be five values, separated by comma
* Example are: 1,2,3,4,5
* The app will review your entered data
* If incorrect data is entered the App will invalidate the data and request you enter again
* If correct data is entered, the app will respond with submitted successfully

Response of Data entered by user.

![image](https://user-images.githubusercontent.com/122373462/235654563-b28d13d0-35fe-4ea1-b159-49dd867b5882.png)


Response to invalid data entered by user and the error message assking user to try again.

![image](https://user-images.githubusercontent.com/122373462/235655135-ad818423-e3a3-4e38-aa7c-af3969a0858b.png)

Verification of valid data eneterd by user printed out in terminal

![image](https://user-images.githubusercontent.com/122373462/235655402-25519713-fc52-496a-a582-37d786f6caa6.png)

Value added to expense worksheet is the same as user information is updated.

![image](https://user-images.githubusercontent.com/122373462/235657482-3033a4f6-8c9a-431b-b230-5f6cde0649b7.png)


## Creating the Paris holiday app

The inspiration for creating this app was drawn from love-sandwiches and the tools that was used to complete the creation are listed below.

1. `heroku/python`
2. `heroku/nodejs`
3. Enable google drive API
4. google credential authentication
5. pyfiglet installation

## Implemented features

. The file data used in this app is originally from an excel sheet stored in google drive and on google drive created credentials from google library and enabling API to interact through the terminal.

## Bugs

. I was entering an integer values but I wanted a strings since the app is for user to submit documents and not 1,2,3 format which is int
I fixed this by not converting the input string to integer.


| **Test                         | **Expected                                     | **Outcome   |

| Run run.py                     | Please enter data here                         | As Expected |
| Input i,2,3,                   | Loads data are invalid                         | As Expected |
| Input i,2,3,4,5                |      Loads data are valid                      | As Expected |
| Valid data update expensesheet |     Expense worksheet updated successfully     | As Expected |


## CI Python Linter Validation
![image](https://user-images.githubusercontent.com/122373462/235699591-3e2f6cf7-8834-4399-a348-39c579ca690b.png)


## Technologies

. Python is the programming language used to produce the game.

. GitHub was used to hold the game repository files.

. Gitpod and CodeAnywere were used for the coding environment.

. Heroku was used to deploy the game to the web.


## Version Control

Version control was maintained using git within GitPod and CodeAnywhere to push code to the main repository.

. From the Gitpod terminal use "git add .", which tells git you would like to make changes/updates to the files.

. Then use "git commit -m (plus a comment)", which commits the changes and updates the files.

. Then use the "git push" command, which pushes the committed changes to the main repository.

. To go back and forth between Gitpod and CodeAnywhere workspaces, use the command "git pull" to make sure all data has been brought over before working from the new space.


## Page Deployment

. Heroku CLI was used for this game's deployment. Directions on how to do that are as follows:

. After creating an account and logging in, click "New" to create a new app from the dashboard.

. Choose app's unique name and select your region; press "Create app".

. Go to "Settings" and navigate to Config Vars.

. Add Config Vars.

. This app used only one:
. KEY = PORT : VALUE = 8000.
. Add buildpacks Python and NodeJS - in this order.

. Now you may click the Deploy tab.

. Scroll Down to Deployment Method and select GitHub.

. Select repository to be deployed and connect to Heroku.

. Scroll down to deploy:

. Option 1 is selecting Automatic deploys (Will Update Automatically with every "git push"). This is what I chose for this project.

. Option 2 is selecting Manual deploy (Needs to be manually redeployed after every change, via Heroku deploy tab)

## Credits

. Love sandwiches videos AJGreaves 

. Much of the run_game function was inspired by (and learned from) Code Institute's walkthrough project: love_sandwiches

. For Python code functionality, I code from: python.org, w3schools, and stackoverflow
















Happy coding!

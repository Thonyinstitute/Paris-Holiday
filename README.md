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

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

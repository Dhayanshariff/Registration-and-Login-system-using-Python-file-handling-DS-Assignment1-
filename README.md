# Registration and Login system using Python and file-handling


# Contents
- Introduction
- Python Modules used
- How to use
- Important Note

# Introduction
This is a simple Registration and Login system achieved using Python and file handling. 

Here new users can register themselves by providing their Email ID and a secure Password. 

Once they have done the same, they can log in to their account and they can view or reset thier password if they have forgotten the same.

Password validations are done in both **registration** phase and **forgot password** phase.

Screen clearing methods (**os.system("cls||clear")**) and sleep method (**sleep()**) are used to give a slight experience similar to a Web application rather than a console with cluttered screen (from previous inputs).

There are options given in required places to return to Home screen.

# Pyhton Modules used
The following Modules are used in the python program
- **re**        -> for using regular expressions to Validate Email ID and Password
- **stdiomask** -> for hiding the password which user inputs and replacing with '*'
- **csv**       -> for handling csv file where we store the credentials
- **os**        -> for clearing the previous input and output from screen for a simple look
- **time**      -> **sleep()** method for adding delay in the execution of a program to give a web app experience

# How to use
Once the program is executed, it wait for user input - 'R' or 'L'

![image](https://user-images.githubusercontent.com/118370660/204839968-ec94842a-dee0-4176-8f4a-dcfce97a4f9d.png)

If the user does not have an account and this is the first time they want to access this system, they need to enter 'R' to Register with their Email ID and a secure password.

![image](https://user-images.githubusercontent.com/118370660/204841753-30266d31-d156-4577-9cbe-f122ac69f498.png)

If the user enters an invalid mail id, it will ask user to enters a valid mail id and will take them to previous screen for the same.

![image](https://user-images.githubusercontent.com/118370660/204841146-45f7bb27-350c-4d7a-b702-d40f4a2ddf55.png)

If the user enters an Email ID which already exists, then it will show as below and wait for corresponding input.

![image](https://user-images.githubusercontent.com/118370660/204845969-ea2e22b6-6710-47d1-b04a-2f87a21658bb.png)

Once a valid email id is entered, it will show the criteria for a strong and acceptable password and will wait for user to enter the password.

![image](https://user-images.githubusercontent.com/118370660/204842211-169b43ab-05f5-4d52-9b22-1334c46b1fd3.png)

If the password does not meet any of the criteria, it will show the missing criteria, so that user can correct and re enter a valid password.

![image](https://user-images.githubusercontent.com/118370660/204842785-3746be3f-b579-4fca-b403-b6b4ea9fa2f8.png)

Once a valid password is entered, the program will prompt user to confirm the same password. If the passwords do not match, it will repeat the same steps again.

![image](https://user-images.githubusercontent.com/118370660/204843414-6ab7afb2-d349-40c7-b6f8-d0be3dc0addf.png)

Once password is correctly confirmed by the user, the console will shortly show that the account is registered successfully and will automatically redirect user to login Screen.

![image](https://user-images.githubusercontent.com/118370660/204844320-47d7b48b-800c-4236-b00b-f8c326c7ced3.png)

If the user tries to login with some invalid Email ID which is not present in the system, then the console will show below screen and automatically redirect to Home screen. 

![image](https://user-images.githubusercontent.com/118370660/204844894-a806d448-68bc-49cd-976a-4e3a3f7deaa5.png)

While logging in, if the user enters the incorrect password, then an alert like below is shown and waits for user input to decide whether to allow user **re-enter** the password or to **show** forgot password options or to go to **home** screen.

![image](https://user-images.githubusercontent.com/118370660/204847907-180a4cab-3eae-42cb-9d3e-98009d0576f8.png)


![image](https://user-images.githubusercontent.com/118370660/204847743-2c14c38a-55b3-413b-bd77-cdc2d7e9dd9b.png)

If the user wishes to re-enter the password, it will take them to login screen where they can try login with correct passsword again. If the user has forgotten their password, they can select the forgot password option and it will show the below choices.

![image](https://user-images.githubusercontent.com/118370660/204848661-16d0dd55-c420-4400-af73-7adbbf3b3afe.png)

If the user selects the view option, the password will be shown for approximately 4 seconds and then it will be automatically redirected to login screen.

![image](https://user-images.githubusercontent.com/118370660/204854991-3a92d294-2c9c-4199-91da-1e39acaf3d0c.png)

If the user selects the reset password option, it will be redirected to Reset password Screen where the user can reset thier password. If the entered password and confirm password does not match or the password does not meet the criteria, it will ask again for other valid password (Similar to registration step).

![image](https://user-images.githubusercontent.com/118370660/204850040-74bfc785-5159-4727-918d-68ced01ef706.png)

Once the password has been reset by user, then the screen will be automatically redirected to login screen.

![image](https://user-images.githubusercontent.com/118370660/204850978-972fabb2-9c38-4f35-aa3a-bea8d67a9e14.png)

Once the user enters correct email ID and password (or the updated password if he has reset the same), then they will be logged in to system and shown following message.

![image](https://user-images.githubusercontent.com/118370660/204851627-dad9da96-a475-4755-a5f0-8e658d41fc7a.png)

If the presses the 'Enter' key in keyboard, they will be logged out andredirected to home screen.

![image](https://user-images.githubusercontent.com/118370660/204852057-16bbcbab-22aa-49d0-9dc1-9b88a117ae84.png)

![image](https://user-images.githubusercontent.com/118370660/204852117-efbbe8c9-3414-4e73-afbd-f057500503f9.png)

At any step in the program, if user enters an invalid input other than the mentioned choices, then an alert like below is shown for a few seconds and then the program will automatically redirect to the previous screen to ask the input again

![image](https://user-images.githubusercontent.com/118370660/204846722-82c608ac-8f79-4f0f-beea-8c75e3cddd58.png)

# Important Note
- Please make sure that the modules are available and they need to be installed if not automatically imported by your IDLE or Compiler.
- The screen clearing methods (**os.system("cls||clear")**), requires the program to be run on windows, mac or linux based IDLE or compilers.

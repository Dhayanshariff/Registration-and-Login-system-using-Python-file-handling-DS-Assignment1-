import re
import stdiomask
import csv
import os
from time import sleep


def choice(): #This function gets the user input and based on that calls Functions for Registering or Logging in
  print("             Welcome\n             =======")
  ch = input("\n Enter R for Registration (New User)\n  Enter L for Login (Existing User)\n")
  
  if ch.lower() == 'r':
    os.system("cls||clear")
    email_id()
    print("Password should contain\n1)Length of 5 to 16 characters\n2)atleast One Special character\n3)atleast One Lowercase character\n4)atleast One Uppercase character\n5)atleast One Number")
    password()
    os.system("cls||clear")
    register()
    
  elif ch.lower() == 'l':
    os.system("cls||clear")
    login()
    
  else:
    os.system("cls||clear")
    print("Invalid input!!!")
    sleep(1)
    os.system("cls||clear")
    choice()


def email_id(): #This function Validates if the Email ID given by user for Registering satisfies the email id criteria given in document. If the given email id is already existing, it will call user_exists() function
  cred_list = []
  print("Register Account\n======== =======")
  reg_email_id = input("Enter your Email ID:")
  Email_id = reg_email_id.lower()
  cred_file = open('Credentials.csv','r')
  cred_reader_object = csv.reader(cred_file)
  
  for cred in cred_reader_object:
   cred_list.append(cred)
    
  cred_file.close()
  if any(Email_id.lower() == x[0].lower() for x in cred_list):
    user_exists()
    
  else:
    Email_id_check = '^[a-zA-Z][^@\.\s]+@{1}[^@\.\s]+\.{1}[^@\.\s]+$'  
    Email_id_matches = re.findall(Email_id_check,Email_id)
    
    if len(Email_id_matches) == 1 and str(*Email_id_matches) == Email_id:
      global Valid_Email 
      Valid_Email = Email_id
      
    else:
      os.system("cls||clear")
      print("Enter a valid email ID\nExamples: ram92@gmail.com \n          Kavitha@yahoo.com\n\nRedirectng to Registeration Screen")
      sleep(3)
      os.system("cls||clear")
      email_id()
      

def user_exists(): #This functions gets called if the email id which is being tried to register is already registered
  os.system("cls||clear")
  user_exists_ip = input("Sorry, the mentioned email ID is already registered :( \n\nPlease enter R for registering with other email ID\n                   or\n           Please enter L to login\n")
  if user_exists_ip.lower() == 'r':
    os.system("cls||clear")
    email_id()
    
  elif user_exists_ip.lower() == 'l':
    os.system("cls||clear")
    login()
    
  else:
    print("Invalid selection!!!")
    sleep(1)
    user_exists()


def password(): #This function validates the password according to given requirement (During Registration and also during Resetting the password when forgotten)
  pwd = stdiomask.getpass("Enter your Password:", '*')
  if len(pwd) < 5 or len(pwd) > 16 :
    print("Password should contain Length of 5 to 16 characters")
    password()
    
  elif len(re.findall('[^a-zA-Z0-9]',pwd)) == 0:
    print("Password should contain atleast One Special character")
    password()
    
  elif len(re.findall('[a-z]',pwd)) == 0:
    print("Password should contain atleast One lowercase character")
    password()
    
  elif len(re.findall('[A-Z]',pwd)) == 0:
    print("Password should contain atleast One uppercase character")
    password()
    
  elif len(re.findall('[0-9]',pwd)) == 0:  
    print("Password should contain atleast One Number")
    password()
    
  else:
    cnf_pwd = stdiomask.getpass("Confirm your Password again:", '*')
    if cnf_pwd != pwd:
      print("Passwords do not match. Re-enter again")
      password()
      
    else:
      global Valid_Password
      Valid_Password = pwd
      

def register(): #Once the email Id and Password is validated, then this function gets called to store the data in to Credentials.csv file
  cred_list = list()
  cred_list.extend([Valid_Email,Valid_Password])
  f = open('Credentials.csv','a')
  writer_object = csv.writer(f)
  writer_object.writerow(cred_list)
  f.close()
  print("Your account is registered Successfully!!!")
  print("        Login to your account")
  sleep(2.5)
  os.system("cls||clear")
  login()
  

def login(): #This function is called to login(for existing user) 
  global r_email_id
  global r_pwd
  global l1
  print("Login\n=====")
  login_email_id = input("Enter registered email ID:")
  r_email_id = login_email_id.lower()
  r_pwd = stdiomask.getpass("Enter your account password:")
  os.system("cls||clear")
  l1 = []
  f = open('Credentials.csv','r')
  reader_object = csv.reader(f)
  
  for cred in reader_object:
   l1.append(cred)
  f.close()
  
  if [r_email_id,r_pwd] in l1:
    print("You have logged in Successfully")
    input("   Press Enter key to Logout")
    os.system("cls||clear")
    print("You have logged out successfully")
    print("Redirecting to Home Screen. Please wait...")
    sleep(1.8)
    os.system("cls||clear")
    choice()
  
  elif any(r_email_id == x[0] for x in l1):
    selection()
    
  else:
    os.system("cls||clear")
    print('''     User not registered!!!\n\nKindly Login with a registered email-ID\n               or\n   Register if you are a new user''')
    print("Redirecting to Home Screen. Please wait...")
    sleep(4)
    os.system("cls||clear")
    choice()
    

def selection(): #This function is called if user provides Wrong password
  print("Login\n=====")
  sel = input('''         Password is Incorrect!!!\n\n  Enter R to Re-enter your credentials or
Enter F if you have forgotten your password or
       Enter H to go to home screen\n''')
  if sel.lower() == 'r':
    os.system("cls||clear")
    login()
    
  elif sel.lower() == 'f':
    os.system("cls||clear")
    forgot()
    
  elif sel.lower() == 'h':
    os.system("cls||clear")
    choice()
    
  else:
    print("Invalid selection!!!")
    sleep(1)
    os.system("cls||clear")
    selection()
    

def forgot(): #This function provides options if user selects 'Forgot Password' option in previous step
  global l2
  l2 = []
  print("Password options\n======== =======\n")
  forgot_ip = input("Enter R to reset your Password or\nEnter V to view your Password or\n Enter H to go to home screen\n")
  if forgot_ip.lower() == 'r': #This part resets the password for the given user
    os.system("cls||clear")
    print("Reset Password\n===== ========")
    print("Password should contain\n1)Length of 5 to 16 characters\n2)atleast One Special character\n3)atleast One Lowercase character\n4)atleast One Uppercase character\n5)atleast One Number")
    password()
    
    for each in l1:
      if each[0] == r_email_id:
        each[1] = Valid_Password
      l2.append(each)
      
    file = open('Credentials.csv','w')
    writer_obj=csv.writer(file)
    writer_obj.writerows(l2)
    file.close()
    print("Your Password is updated successfully.")
    print("Please login again")
    sleep(2.2)
    os.system("cls||clear")      
    login()
    
  elif forgot_ip.lower() == 'v': #This part shows the password in screen for the given user
    os.system("cls||clear")
    print("View Password\n==== ========")
    
    for each in l1:
      if each[0] == r_email_id:
        print("Your Passsword is:",each[1])
        print("Please make a note before we redirect you to Home Screen")
        sleep(4.2)
        os.system("cls||clear")
        login()
        
  elif forgot_ip.lower() == 'h':
    os.system("cls||clear")
    choice()
    
  else:
    print("Invalid selection!!!")
    sleep(1)
    os.system("cls||clear")
    forgot()    

choice()
#This is the main function which runs once the program is executed
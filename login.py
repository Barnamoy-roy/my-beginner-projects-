# basic login system design algorithm along with signup

# sign up algorithm

import time                                                      #importing time module for pause effects

print("SIGN UP SYSTEM")
print()
userid = str(input("enter your userid: "))
email_address = str(input("enter your email address: "))
pass1 = str(input("enter your password: "))
pass_check = str(input("confirm the password: "))

if pass_check != pass1:                                          # condition of if the confirm password is not equal to the entered password
    print()
    print("please confirm the password again")

else:
     print()
     print("signup is completed!! please login to access the mainframe")
     print()
     #now login system

     print("LOGIN SYSTEM")
     print()                                                     #user is asked to enter the userid and password for login
     user = str(input("enter your userid: "))
     pass2 = str(input("enter your password: "))

     if user == userid and pass2 == pass1:                       #if the userid and sign up username are equal and password is also equal then the login is completed
       time.sleep(2)
       print("Please wait...")                                   #time.sleep() is used to pause the code execution for a certain amount of time in seconds
       time.sleep(2)
       print("access granted!")
       time.sleep(2)
       print("now you can access the mainframe")
     elif user == userid and pass2 != pass1:                     #the elif and else statements layout the other possible condition and print the statement regarding to it
       print('incorrect password! please try again')
     elif user != userid and pass2 == pass1:
       print("incorrect userid! please try again")
     else:
       print("incorrect credentials please try again")           #basic login and signup system is now completed




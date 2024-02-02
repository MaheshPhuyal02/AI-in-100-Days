import os
from database import database

os.system("cls")

db = database()

print("\n\nWelcome to Misha Bank Ltd. \n\n".center(50))
mode = int(input("Press 1 to login, 2 to register : "))

if mode == 1:
    email = input("Enter email : ")
    password = input("Enter password : ")
    if db.checkPassword(email, password):
         print("Login Successfully.")
    else:
         print("Email or password incorrect.")  
            
elif mode == 2:
     email = input("Enter email : ")
     password = input("Enter password : ")
     if db.register(email, password):
          a = input("Register successfully. Press a to login : ")
          if a == 'a':
               if db.checkPassword(email=email, password=password):
                    print("Login Successfully.")
               

input("")

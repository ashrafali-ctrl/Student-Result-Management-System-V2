import os
from admin import admin
from student import student
from database import connection

def security(a_pass):
      with open ("security.txt","r") as file:
                for password in file:
                      if password.strip() == a_pass:
                            return "granted"
      return "invalid"

while True:
    os.system("cls")
    print("----- STUDENT RESULT MANAGEMENT SYSTEM -----")
    print("1. ADMIN PORTAL (Secured)")
    print("2. STUDENT RESULT (For Student)")
    print("3. Exit")
    choice=input("=> ").strip().upper()
    if choice in ("1", "ADMIN"):
            print("-> Welcome to Admin Portal, for entering this you must enter password")
            a_pass=input("Enter Password : ")
            result=security(a_pass)
            if result == "granted":
                input("\nACCESS GRANTED, Pres Enter to continue ...")
                admin()
            else:
                print("! -- INVALID PASSWORD -- !")
    elif choice in ("2", "STUDENT"):
          student()
            
    elif choice in ("3", "EXIT"):
            print("Exiting...")
            connection.close()
            break
    else:
            print("***** INVALID CHOICE *****")
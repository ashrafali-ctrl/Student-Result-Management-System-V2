import os
import database
import calculations

def adding_students():    #ADDING NEW STUDENT RECORD
    branch="BCA-AI"
    os.system("cls")
    hall_num=input("ENTER HALL TICKET NUMBER          \t: ").upper()
    data = database.valid(hall_num)
    if data is not None:
        print("--- !THIS HALL TICKET NUMBER IS ALREADY EXIST! ---")
        input("press ENTER to continue... ")
        return    
    std_name=input("Enter Name of the Student               : ").upper()
    sem=input("Enter Semester Number                   : ")
    year=input("Enter Academic Year                     : ")
    print("-----Marks Memo-----")
    py_marks=database.get_marks("Python Programming")
    ds_marks=database.get_marks("Data Structures")
    dbms_marks=database.get_marks("Data Base Management System (DBMS)")
    cn_marks=database.get_marks("Computer Networks")
    os_marks=database.get_marks("Operating System")
    database.db_insert(hall_num,std_name,branch,sem,year,py_marks,ds_marks,dbms_marks,cn_marks,os_marks)
    print("--- DETAILS SUCCESSFULLY INSERTED ---")
    input("\npress ENTER to continue...")

def searching_students():   #SEARCHING FOR STUDENT RECORD FROM DATA BASE
     hall_num=input("Enter hall-ticket numbere : ".title()).upper()
     std_data=database.searching_student(hall_num)
     if std_data is None:
        print("------- !DATA NOT FOUND! -------")
        input("\npress ENTER to continue...")
        return
     os.system("cls")
     print("+",'-' *52,"+")
     print(f"|{'STUDENT INFORMATION':^54}|")
     print("+",'-' *52,"+")
     print(f"| {'Hall Ticket Number':<20} : {std_data["hall_num"]:<30}|")
     print(f"| {'Name':<20} : {std_data["name"]:<30}|")
     print(f"| {'Branch':<20} : {std_data["branch"]:<30}|")
     print(f"| {'Semester':<20} : {std_data["semester"]:<30}|")
     print(f"| {'Academic Year':<20} : {std_data["academic_year"]:<30}|")
     print(f"| {'Python Programming':<20} : {std_data["python_marks"]:<30}|")
     print(f"| {'Data Structures':<20} : {std_data["ds_marks"]:<30}|")
     print(f"| {'DBMS':<20} : {std_data["dbms_marks"]:<30}|")
     print(f"| {'Computer Networks':<20} : {std_data["cn_marks"]:<30}|")
     print(f"| {'Operating System':<20} : {std_data["os_marks"]:<30}|")
     print("+------------------------------------------------------+")
     input("\npress ENTER to continue...")

def displaying_students():  #DISPLAYING ALL STUDENT RECORDS FROM DATA BASE
    os.system("cls")
    print("=" * 80)
    print(f"|{'ALL STUDENT RECORDS':^78}|")
    print("=" * 80)
    print(f"| {'Hall Ticket':<15}{'Name':<25}{'Branch':<10}{'Semester':<10}{'Academic Year':<15}  |")
    print("-" * 80)
    count=0
    students = database.display()
    for std_data in students:
        count +=1
        print(f"| {std_data["hall_num"]:<15}{std_data["name"]:<25}{std_data["branch"]:<10}{std_data["semester"]:<10}{std_data["academic_year"]:<15}  |")
    print("-" * 80)
    print(f"| Total Students : {count:<60}|")
    print("=" * 80)
    input("\npress ENTER to continue...")

def update_students():  #UPDARING STUDENT RECORD 
    hall_num=input("Enter hall-ticket number : ".title()).upper()
    std_data=database.searching_student(hall_num)
    if std_data is None:
        print("------- !DATA NOT FOUND! -------")
        input("\npress ENTER to continue...")
        return
    os.system("cls")
    print("+",'-' *52,"+")
    print(f"|{'STUDENT CURRENT INFORMATON':^54}|")
    print("+",'-' *52,"+")
    print(f"| {'Hall Ticket Number':<20} : {std_data["hall_num"]:<30}|")
    print(f"| {'Name':<20} : {std_data["name"]:<30}|")
    print(f"| {'Branch':<20} : {std_data["branch"]:<30}|")
    print(f"| {'Semester':<20} : {std_data["semester"]:<30}|")
    print(f"| {'Academic Year':<20} : {std_data["academic_year"]:<30}|")
    print(f"| {'Python Programming':<20} : {std_data["python_marks"]:<30}|")
    print(f"| {'Data Structures':<20} : {std_data["ds_marks"]:<30}|")
    print(f"| {'DBMS':<20} : {std_data["dbms_marks"]:<30}|")
    print(f"| {'Computer Networks':<20} : {std_data["cn_marks"]:<30}|")
    print(f"| {'Operating System':<20} : {std_data["os_marks"]:<30}|")
    print("+------------------------------------------------------+")
    print("**********UPDATE STUDENT RECORD**********")
    calculations.update_std_record(std_data["hall_num"])
    print("--- !STUDENT RECORD UPDATED SUCCESSFULLY! ---")
    input("\npress ENTER to continue...")

def deleting_students():    #DELETING STUDENT RECORD FROM DATA BASE
    hall_num=input("Enter hall-ticket number : ".title()).upper()
    std_data=database.searching_student(hall_num)
    if std_data is None:
        print("--- !DATA NOT FOUND! ---")
        input("\npress ENTER to continue...")
        return
    os.system("cls")
    print("=" * 80)
    print(f"|{'STUDENT RECORD':^78}|")
    print("=" * 80)
    print(f"| {'Hall Ticket':<15}{'Name':<25}{'Branch':<10}{'Semester':<10}{'Academic Year':<15}  |")
    print("-" * 80)
    print(f"| {std_data["hall_num"]:<15}{std_data["name"]:<25}{std_data["branch"]:<10}{std_data["semester"]:<10}{std_data["academic_year"]:<15}  |")
    print("=" * 80)
    while True:
        admin_choice=input("If you want to delete this record -> Enter 'YES' otherwise 'NO : ".title()).lower()
        if admin_choice == "yes":
            database.delete_student_db(hall_num)
            break
        elif admin_choice.lower()=="no":
            print("-----record was not deleted-----".upper())
            break
        else:
            print("Please enter only 'YES' or 'NO'.".title())
    input("\npress ENTER to continue...")

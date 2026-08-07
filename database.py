import os
import sqlite3
connection = sqlite3.connect("student_result.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def valid(hall): #VALIDATING THE HALL TICKET NUMBER, IT IS ALREADY EXIT OR NOT
    data=None
    cursor.execute("select name from students where (hall_num = ?)",(hall,))
    data = cursor.fetchone()
    return data

def db_insert(hall,name,branch,sem,year,py,ds,dbms,cn,os):    #INSERTING STUDENT DETAILS INTO DATA BASE
    cursor.execute("""INSERT into students (
    hall_num,name,branch,semester,academic_year,python_marks,ds_marks,dbms_marks,cn_marks,os_marks) VALUES (
    ?,?,?,?,?,?,?,?,?,?)""",(hall,name,branch,sem,year,py,ds,dbms,cn,os))
    connection.commit()

def searching_student(hall):    #RETURING STUDENT DATA FROM DATA BASE
     std_data=None
     cursor.execute("select * from students where (hall_num= ? )",(hall,))
     std_data=cursor.fetchone()
     if std_data == None:
         print("----- !DATA  NOT FOUND! -----")
     return std_data

def update_std_db(ad_choice,choice,hall):   #RE-ENTERING UPDATED STUDENT RECORD INTO THE DATA BASE
    cursor.execute(f"update students set {ad_choice} = ? where (hall_num = ? )",(choice,hall))
    connection.commit()
    print(f"----- {ad_choice} is updated to {choice} -----")

def delete_student_db(hall):    #DELETING STUDENT RECORD FROM DATA BASE
    cursor.execute("delete from students where (hall_num = ?)",(hall,))
    connection.commit()
    print("**********Deleted successfully**********".upper())
    input("\npress ENTER to continue...")

def display():
    cursor.execute("select * from students")
    students=cursor.fetchall()
    return students

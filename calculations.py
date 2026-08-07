import database

def get_marks(subject):     #VERIFYING MARKS IS VALID OR NOT
    while True:
        marks_d=input(f"Enter marks of {subject} : ".title())
        if marks_d.isdigit():
            marks=int(marks_d)
            if marks >= 0 and marks <=100:
                return marks
            else:
                print("marks should be between 0 to 100.")
        else:
            print("!-INVALID DATA ENTERED-!")

def s_result(marks):   #CHECKING WHETHER THE RESULT OF A SUBJECT IS PASS OR FAIL
    if marks < 40:
        return "Fail"
    else:
        return "Pass"

def grade(marks):     #GRADE POINTS AND GRADE
     if marks >= 90:
        grade_points=10
        return "O", grade_points
     elif marks >= 80:
        grade_points=9
        return "A+", grade_points
     elif marks >= 70:
        grade_points=8
        return "A",grade_points
     elif marks >= 60:
        grade_points=7
        return "B+",grade_points
     elif marks >= 50:
        grade_points=6
        return "B",grade_points
     elif marks >= 40:
        grade_points=5
        return "C",grade_points
     else:
        grade_points=0
        return "F",grade_points

def sgpa(py,ds,dbms,cn,os):    #CALCULATING SGPA
     py_cr,ds_cr,dbms_cr,cn_cr,os_cr=4,4,3,3,3
     total=(py*py_cr + ds*ds_cr + dbms*dbms_cr + cn*cn_cr + os*os_cr)/17
     sgpa=round(total,2)
     return sgpa

def calculate_result(std_data):    #CALCULATING RESULT
#     py_marks,ds_marks,dbms_marks,cn_marks,os_marks=int(std_data[5]),int(std_data[6]),int(std_data[7]),int(std_data[8]),int(std_data[9])
     total=std_data["python_marks"]+std_data["ds_marks"]+std_data["dbms_marks"]+std_data["cn_marks"]+std_data["os_marks"]
     py_r=s_result(std_data["python_marks"])
     ds_r=s_result(std_data["ds_marks"])
     dbms_r=s_result(std_data["dbms_marks"])
     cn_r=s_result(std_data["cn_marks"])
     os_r=s_result(std_data["os_marks"])
     if std_data["python_marks"] < 40 or std_data["ds_marks"] < 40 or std_data["dbms_marks"] < 40 or std_data["cn_marks"] < 40 or std_data["os_marks"] < 40:
          result="FAIL"
     else:
          result="PASS"
     percentage=total/5
     py_grade,py_grade_p=grade(std_data["python_marks"])
     ds_grade,ds_grade_p=grade(std_data["ds_marks"])
     dbms_grade,dbms_grade_p=grade(std_data["dbms_marks"])
     cn_grade,cn_grade_p=grade(std_data["cn_marks"])
     os_grade,os_grade_p=grade(std_data["os_marks"])
     SGPA=sgpa(py_grade_p,ds_grade_p,dbms_grade_p,cn_grade_p,os_grade_p)
     return py_r,ds_r,dbms_r,cn_r,os_r,py_grade,ds_grade,dbms_grade,cn_grade,os_grade,percentage,total,SGPA,result

def update_std_record(hall):    #TAKING UPDATED DETAILS FROM ADMIN
    print(f"HALL TICKET NUMBER : {hall}")
    while True:
        choice=input("Enter what you want to update (Student Information or Student Marks): ").lower()
        if choice in ("student information", "info"):
                while True:
                    print("Enter what you want to update (=> name, => branch, => semester, => academic_year )")
                    ad_choice=input("=> ").lower()
                    if ad_choice in ("name", "branch", "semester", "academic_year"):
                        choice = input(f"enter {ad_choice} : ".upper()).upper()
                        database.update_std_db(ad_choice,choice,hall)
                        return
                    else:
                        print("------- !INVALID! -------")
        elif choice in ("student marks", "marks"):
                while True:
                    print("Enter which subject marks you want to update (=> python , => Data_Structures= ds, => DBMS, => Computer_Network= cn, => Operating_System= os)")
                    ad_choice=input("=> ").lower()
                    if ad_choice in ("python", "ds", "dbms", "cn", "os"):
                        choice = get_marks(ad_choice)
                        database.update_std_db(ad_choice+"_marks",choice,hall)
                        return
                    else:
                        print("------- !INVALID! -------")
        else:
            print("------- !INVALID! -------")

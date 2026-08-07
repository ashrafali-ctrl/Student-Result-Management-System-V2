import os
from database import searching_student
from calculations import calculate_result
def student():            
            os.system("cls")
            print(f"{'---RESULT MANAGEMENT SYSTEM---':^70}")
            print()
            print("-"*50)
            hall_num = input(" Enter your Hall Ticket Number : ").upper()
            print("-"*50)
            std_data=searching_student(hall_num)
            if std_data is None:
                input("\nPress Enter to return back ...")
                return
            input("\nRESULT FOUND, press ENTER to see ...")
            os.system("cls")
            py_r,ds_r,dbms_r,cn_r,os_r,py_grade,ds_grade,dbms_grade,cn_grade,os_grade,percentage,total,SGPA,result=calculate_result(std_data)
            print("=" * 80)
            print(" " * 28 + "STUDENT RESULT PORTAL")
            print("=" * 80)

            print("\n  +-------------------------------------------------------------------------+")
            print("  |                          STUDENT INFORMATION                            |")
            print("  +----------------------+--------------------------------------------------+")
            print(f"  | Student Name         | {std_data["name"]:<49}|")
            print(f"  | Hall Ticket Number   | {std_data["hall_num"]:<49}|")
            print(f"  | Branch               | {std_data["branch"]:<49}|")
            print(f"  | Semester             | {std_data["semester"]:<49}|")
            print(f"  | Academic Year        | {std_data["academic_year"]:<49}|")
            print("  +----------------------+--------------------------------------------------+")

            print("\n  +---------------------------------------------------------------------+")
            print("  |                              RESULT SHEET                           |")
            print("  +----+----------------------+-------+---------+---------+-------------+")
            print("  | No | Subject              | Grade | Credits | Marks   | Result      |")
            print("  +----+----------------------+-------+---------+---------+-------------+")

            print(f"  | 1  | Python Programming   | {py_grade:^5} |    4    | {std_data["python_marks"]:^7} | {py_r:^11} |")
            print(f"  | 2  | Data Structures      | {ds_grade:^5} |    4    | {std_data["ds_marks"]:^7} | {ds_r:^11} |")
            print(f"  | 3  | DBMS                 | {dbms_grade:^5} |    3    | {std_data["dbms_marks"]:^7} | {dbms_r:^11} |")
            print(f"  | 4  | Computer Networks    | {cn_grade:^5} |    3    | {std_data["cn_marks"]:^7} | {cn_r:^11} |")
            print(f"  | 5  | Operating Systems    | {os_grade:^5} |    3    | {std_data["os_marks"]:^7} | {os_r:^11} |")

            print("  +----+----------------------+-------+---------+---------+-------------+")
 
            print()
            print(f"  Total Marks : {total} / 500")
            print(f"  Percentage  : {percentage:.2f} %")
            print(f"  SGPA        : {SGPA}")
            print(f"  Result      : {result}")
            print()
            print("=" * 84)
            print()
            input("\nPress Enter to return back ...")
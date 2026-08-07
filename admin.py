import os
import admin_operations
def admin ():
    while True:
                        os.system("cls")
                        print("********** ADMIN PORTAL **********")
                        print("1. Add Student")
                        print("2. Search Student")
                        print("3. Display Students")
                        print("4. Update Student")
                        print("5. Delete Student")
                        print("6. Exit")
                        admin_choice = input("=> ").strip().upper()
    
                        if admin_choice in ("1", "ADD"):
                            admin_operations.adding_students()
                        elif admin_choice in ("2", "SEARCH"):
                            admin_operations.searching_students()
                        elif admin_choice in ("3", "DISPLAY"):
                            admin_operations.displaying_students()
                        elif admin_choice in ("4", "UPDATE"):
                            admin_operations.update_students()
                        elif admin_choice in ("5", "DELETE"):
                            admin_operations.deleting_students()
                        elif admin_choice in ("6", "EXIT"):
                            print("Exiting as Admin ...")
                            return
                        else:
                            print("*** INVALID CHOICE ***")
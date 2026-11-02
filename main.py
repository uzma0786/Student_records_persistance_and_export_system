import json
import csv
import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR,"students.json")
CSV_FILE = os.path.join(BASE_DIR,"students.csv")
LOG_FILE = os.path.join(BASE_DIR,"activity_log.txt")

def load_students():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE,"r") as file:
            students = json.load(file)
            return students
    else:
        return {}

def save_students(std_dict):
    with open(JSON_FILE,"w") as file:
        json.dump(std_dict,file,indent=4)
    print("student record saved successfully...")

def validate_student(student_id,marks,students):
    if student_id in students:
        print("student id already exist..")
        return False
    for mark in marks.values():
        if mark < 0 or mark > 100:
            print("Mark must be between (0-100)..")
            return False
    return True

def add_student(students):
    std_id = input("\nenter student id: ")
    name = input("enter name: ")
    department = input("enter department: ")
    marks = {}
    python_m = float(input("enter python marks: "))
    marks["python"] = python_m
    maths_m = float(input("enter maths marks: "))
    marks["maths"]=maths_m
    dbms_m = float(input("enter dbms marks: "))
    marks["dbms"]=dbms_m
    validate = validate_student(std_id,marks,students)
    if validate:
        students[std_id] = {
            "name":name,
            "department":department,
            "marks":marks
        }
        save_students(students)
        write_log(f"Student {std_id} added")

def search_student(students):
    std_id = input("\nenter student id to search: ")
    if std_id in students:
        print("Name:",students[std_id]['name'])
        print("Department:",students[std_id]['department'])
        print("Marks:",students[std_id]['marks'])
    else:
        print("student not found!")

def display_students(students):
    for id,details in students.items():
        print("\nStudent ID:",id)
        print("Name:",details['name'])
        print("Department:",details['department'])
        print("Marks:",details['marks'])

def export_csv(students):
    with open(CSV_FILE,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Student ID","Name","Department",
            "Python","Maths","DBMS"
        ])
        for student_id,details in students.items():
            writer.writerow([
                student_id,
                details['name'],
                details['department'],
                details['marks']['python'],
                details['marks']['maths'],
                details['marks']['dbms']
            ])
    write_log("student record exported to CSV")

def write_log(activity):
    with open(LOG_FILE,"a") as file:
        current_time = datetime.datetime.now()
        file.write(f"{current_time} - {activity}\n")

def read_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE,"r") as file:
            data = file.read()
            print(data)
    else:
        print("Activity log is not found")

def read_one_line():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE,"r") as file:
            data = file.readline()
            print(data)
    else:
        print("Activity log not found.")

def read_all_lines():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE,"r") as file:
            data = file.readlines()
            print(data)
    else:
        print("Activity log is not found.")

def testing_writing_method():
    with open(LOG_FILE,"a") as file:
        file.write("This line is writen use write().\n")
        list = [
            "First line is written using writelines(),\n",
            "Second line is written using writelines().\n"
        ]
        file.writelines(list)
    print("Text writting methods are used.")

def json_string_demo(students):
    json_string = json.dumps(students,indent=4)
    print("JSON String:")
    print(json_string)

    python_data = json.loads(json_string)
    print("Converting json string to python data:")
    print(python_data)


students = load_students()
if students is None:
    print("Program stopped because students.json is corrupted.")
else:
    while True:
        print("\n=====STUDENT RECORD SYSTEM=====")
        print("1. ADD RECORD")
        print("2. SEARCH STUDENTS")
        print("3. DISPLAY ALL STUDENTS")
        print("4. EXPORT TO CSV")
        print("5. READ ACTIVITY LOG")
        print("6. READ FIRST LINES")
        print("7. READ ALL LINES")
        print("8. TEST WRITING METHODS")
        print("9. JSON STRING DEMO")
        print("10. EXIT")

        choice = int(input("enter your choice(1-10): "))
        if choice == 1:
            add_student(students)
        elif choice == 2:
            search_student(students)
        elif choice == 3:
            display_students(students)
        elif choice == 4:
            export_csv(students)
        elif choice == 5:
            read_log()
        elif choice == 6:
            read_one_line()
        elif choice == 7:
            read_all_lines()
        elif choice == 8:
            testing_writing_method()
        elif choice == 9:
            json_string_demo(students)
        elif choice == 10:
            print("Thank you!")
            break
        else:
            print("Invalid choice, try again..")
    



print("\n ****************************GEETA BAAL BHARTI SENIOR SECONDARY SCHOOL*************************\n")
print(" ************************Project - School_Management_System*******************\n")
print(" ************  DESIGNED AND MAINTAINED BY___ \n")
print(" ********  KAKUL JAIN - CLASS XII A - ROLL NUMBER - 17\n")
print(" ********  SAPNA  - CLASS XII A - ROLL NUMBER - 07\n")



import mysql.connector

# Function to connect to the MySQL database
def connect_db():
    return mysql.connector.connect(

            host="localhost",
        user="root",  # Replace with your MySQL username
        password="Mysql@9897",  # Replace with your MySQL password
        database="school_management"  # Database name
    )

# Student Management Functions
def add_student(name, age, grade):
    """Add a new student to the database."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    db.commit()  # Commit the transaction
    cursor.close()
    db.close()
   
def view_students():
    """Retrieve and display all students from the database."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    print("\n--------- STUDENT ADDED SUCCESSFULLY. ------------")
    print("\n--------- DETAILS OF ALL STUDENTS. ------------")
    for (id, name, age, grade) in cursor.fetchall():
        
        print("\n"+"_"*80+"\n")
        print(f"ID: {id}, Name: {name}, Age: {age}, Grade: {grade}")
        print("_"*80)
    cursor.close()
    db.close()

def delete_student(student_id):
    """Delete a student from the database by ID."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    db.commit()
    cursor.close()
    db.close()
    print("\n"+"*"*80+"\n")
    print("\n--------- STUDENT DELTED SUCCESSFULLY. ------------")
    print("*"*80)

def update_student(student_id, name, age, grade):
    """Update an existing student's details."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s", (name, age, grade, student_id))
    db.commit()
    cursor.close()
    db.close()
    print("\n--------- STUDENT UPDATED SUCCESSFULLY. ------------")

def search_student(name):
    """Search for students by name."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE %s", (f"%{name}%",))
    results = cursor.fetchall()
    if results:
        for (id, name, age, grade) in results:
         print("-"*80 +"\n")
        print(f"ID: {id}, Name: {name}, Age: {age}, Grade: {grade}")
        print("-"*80 +"\n")
    else:
        print("No students found with that name.")
    cursor.close()
    db.close()

# Class Management Functions
def add_class(class_name):
    """Add a new class to the database."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO classes (class_name) VALUES (%s)", (class_name,))
    db.commit()
    cursor.close()
    db.close()
    print("\n--------- CLASS ADDED SUCCESSFULLY. ------------")

def view_classes():
    """Retrieve and display all classes from the database."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM classes")
    print("\n--------------- DETAILS OF ALL CLASSES. -----------------\n")
    print("|"*90+"\n")
    for (id, class_name) in cursor.fetchall():
        print(f"ID: {id}, Class Name: {class_name}")
    cursor.close()
    db.close()

def delete_class(class_id):
    """Delete a class from the database by ID."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM classes WHERE id = %s", (class_id,))
    db.commit()
    cursor.close()
    db.close()
    print("\n--------- CLASS DELETED SUCCESSFULLY. ------------")

# Teacher Management Functions
def add_teacher(name, subject):
    """Add a new teacher to the database."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO teachers (name, subject) VALUES (%s, %s)", (name, subject))
    db.commit()
    cursor.close()
    db.close()
    print("\n--------- TEACHER ADDED SUCCESSFULLY. ------------")

def view_teachers():
    """Retrieve and display all teachers from the database."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM teachers")
    print("\n--------------- DETAILS OF ALL TEACHERS. -----------------\n")
    print("|"*90+"\n")
    for (id, name, subject) in cursor.fetchall():
        print(f"ID: {id}, Name: {name}, Subject: {subject}")
    cursor.close()
    db.close()

def delete_teacher(teacher_id):
    """Delete a teacher from the database by ID."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM teachers WHERE id = %s", (teacher_id,))
    db.commit()
    cursor.close()
    db.close()
    print("\n--------- TEACHER DELETED SUCCESSFULLY. ------------")

# Assign Student to Class
def assign_student_to_class(student_id, class_id):
    """Assign a student to a class."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO student_classes (student_id, class_id) VALUES (%s, %s)", (student_id, class_id))
    db.commit()
    cursor.close()
    db.close()
  
    print("\n--------- STUDENT ASSIGNED TO CLASS SUCCESSFULLY. ------------")
    
def view_student_classes(student_id):
    """View all classes assigned to a specific student."""
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        SELECT c.id, c.class_name 
        FROM classes c 
        JOIN student_classes sc ON c.id = sc.class_id 
        WHERE sc.student_id = %s
    """, (student_id,))
    print("\n--------------- DETAILS OF STUDENT CLASS. -----------------\n")
    print("|"*90+"\n")
    results = cursor.fetchall()
    if results:
        print(f"Classes for Student ID {student_id}:")
        for (id, class_name) in results:
            print(f"Class ID: {id}, Class Name: {class_name}")
    else:
        
           print("\n--------- NO CLASSES FOUND FOR THIS STUDENT. ------------")
    cursor.close()
    db.close()

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("-"*50)
        print("\n ---------------SCHOOL MNAGEMENT SYSTEM---------------")
        
        print("ENTER 1 -> Add Student")
        print("."*40)
        print("ENTER 2 -> View Students")
        print("."*40)
        print("ENTER 3 -> Delete Student")
        print("."*40)
        print("ENTER 4 -> Update Student")
        print("."*40)
        print("ENTER 5 -> Search Student")
        print("."*40)
        print("ENTER 6 -> Add Class")
        print("."*40)
        print("ENTER 7 -> View Classes")
        print("."*40)
        print("ENTER 8 -> Delete Class")
        print("."*40)
        print("ENTER 9. Add Teacher")
        print("."*40)
        print("ENTER 10 -> View Teachers")
        print("."*40)
        print("ENTER 11 -> Delete Teacher")
        print("."*40)
        print("ENTER 12 -> Assign Student to Class")
        print("."*40)
        print("ENTER 13 -> View Student Classes")
        print("."*40)
        print("ENTER 14 -> Exit")
        print("."*40)
        print("|"*80)
        

        choice = input("\nENTER YOUR CHOICE : ")
        print("|"*80+"\n")
        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '4':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new student name: ")
            age = int(input("Enter new student age: "))
            grade = input("Enter new student grade: ")
            update_student(student_id, name, age, grade)
        elif choice == '5':
            name = input("Enter student name to search: ")
            search_student(name)
        elif choice == '6':
            class_name = input("Enter class name: ")
            add_class(class_name)
        elif choice == '7':
            view_classes()
        elif choice == '8':
            class_id = int(input("Enter class ID to delete: "))
            delete_class(class_id)
        elif choice == '9':
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")
            add_teacher(name, subject)
        elif choice == '10':
            view_teachers()
        elif choice == '11':
            teacher_id = int(input("Enter teacher ID to delete: "))
            delete_teacher(teacher_id)
        elif choice == '12':
            student_id = int(input("Enter student ID to assign: "))
            class_id = int(input("Enter class ID to assign to: "))
            assign_student_to_class(student_id, class_id)
        elif choice == '13':
            student_id = int(input("Enter student ID to view classes: "))
            view_student_classes(student_id)
        elif choice == '14':
            print("|"*90+"\n")
            print("******************************** EXITING THE  PROGRAM *******************************\n")
            print("-"*90)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

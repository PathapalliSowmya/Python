import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="student_management"
)
cursor=conn.cursor()
print("connected Successfully...")
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
class Student:
    def __init__(self,s_id,s_name,s_branch,s_age,s_marks):
        self.name=s_name
        self.id=s_id
        self.branch=s_branch
        self.age=s_age
        self.marks=s_marks
    def display(self):
        print("-----STUDENT DETAILS-----")
        print(f"Student ID : {self.id}")
        print(f"Student Name : {self.name}")
        print(f"Student Branch : {self.branch}")
        print(f"Student Age : {self.age}")
        print(f"student marks : {self.marks}")
student_details=[]
def add_student():
        s_id=int(input("Enter Student ID : "))
        for student in student_details:
            if student.id==s_id:
                print("Student Already Exists")
                return
        s_name=input("Enter Student Name : ")
        s_branch=input("Enter Student Branch : ")
        s_age=int(input("Enter Student Age : "))
        s_marks=float(input("Enter Student Marks : "))
        query="""
        INSERT INTO STUDENTS
        (STUDENT_ID,STUDENT_NAME,BRANCH,AGE,MARKS)
        VALUES(%s,%s,%s,%s,%s)
        """
        values=(s_id,s_name,s_branch,s_age,s_marks)
        cursor.execute(query,values)
        conn.commit()
        print("Student added Successfully....")
def view_students():
    if len(student_details)==0:
        print("No student Found")
    else:
        for student in student_details:
            student.display()

def search_student(student_id):
    for student in student_details:
        if student.id==student_id:
            student.display()
            return
    print("Student Details Not Found")

def update_student(student_id):
    for student in student_details:
        if student.id==student_id:
            student.name=input("Enter New Name : ")
            student.branch=input("Enter New Branch : ")
            student.age=int(input("Enter New Age : "))
            student.marks=float(input("Enter New Marks : "))
            print("Student Updated Successfully...")
            return
    print("Student details Not Found")

def delete_student(student_id):
    for student in student_details:
        if student.id==student_id:
            student_details.remove(student)
            print("Student Deleted Successfully...")
            return
    print("Student Details Not Found")

def calculate_grade(student_id):
    for student in student_details:
        if student.id==student_id:
            if student.marks>=90:
                grade="A+"
            elif student.marks>=80:
                grade="A"
            elif student.marks>=70:
                grade="B"
            elif student.marks>=60:
                grade="C"
            else:
                grade="F"
            print(f"grade : {grade}")
            return
    print("Student Details Not Found")

while True:
    print("-----MENU-----")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student Details")
    print("5.Delete Student")
    print("6.Calculate Grade")
    print("7.Exit")
    choice=input("Enter Your choice :")
    if choice=='1':
        add_student()
    elif choice=='2':
        view_students()
    elif choice=='3':
         student_id=int(input("Enter Student ID : "))
         search_student(student_id)
    elif choice=='4':
        student_id=int(input("Enter Student ID : "))
        update_student(student_id)
    elif choice=='5':
        student_id=int(input("Enter Student ID : "))
        delete_student(student_id)
    elif choice=='6':
        student_id=int(input("Enter Student ID : "))
        calculate_grade(student_id)
    elif choice=='7':
        print("Thank you")
        break
    else:
        print("Invalid choice...Try Again")

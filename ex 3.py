from tkinter import *
from tkinter import simpledialog
#using from tkinter import simpledialog since it is easier and does not require multiplie lines of code for entry

#reading the text file
file = open("studentMarks.txt", "r")
numberOfstudents = int(file.readline())
students = []

for line in file:
    students.append(line.strip().split(","))

file.close()

#calculating coursework marks
def coursework(student):
    return int(student[2]) + int(student[3]) + int(student[4])

#calculating the percentage
def percentage(student):
    return(coursework(student) + int(student[5])) / 160 * 100

#calculating grade
def grade(mark):
    if mark>=70:
        return"A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

#to display the details of the students
def displayStudent(student):
    output.insert(END, "Name: " + student[1] + "\n")
    output.insert(END, "Number: " + student[0] + "\n")
    output.insert(END, "Coursework: " + str(coursework(student)) + "/60\n")
    output.insert(END, "Exam: " + student[5] + "/100\n")
    output.insert(END, "Percentage: " + str(round(percentage(student), 2)) + "%\n")
    output.insert(END, "Grade: " + grade(percentage(student)) + "\n\n")

#to view all the students 
def viewAll():
    output.delete("1.0", END)
    total = 0

    for student in students:
        displayStudent(student)
        total += percentage(student)

    output.insert(END, "Total Students: " + str(len(students)) + "\n")

    if len(students) > 0:
        average = total / len(students)
        output.insert(END, "Average: " + str(round(average, 2)) + "%")

# finding a student
def findStudent():
    number = simpledialog.askstring("Student", "Enter student number:")

    for student in students:
        if student[0] == number:
            return student

    return None


# to view an individual student
def viewIndividual():
    output.delete("1.0", END)
    student = findStudent()

    if student != None:
        displayStudent(student)
    else:
        output.insert(END, "Student not found")


# to find the highest scoring student
def highestScore():
    output.delete("1.0", END)

    if len(students) > 0:
        displayStudent(max(students, key=percentage))


# to find the lowest scoring student
def lowestScore():
    output.delete("1.0", END)

    if len(students) > 0:
        displayStudent(min(students, key=percentage))


# to sort the student records
def sortRecords():
    order = simpledialog.askstring("Sort", "Enter A for ascending or D for descending")

    if order == "A":
        students.sort(key=percentage)
    elif order == "D":
        students.sort(key=percentage, reverse=True)

    viewAll()


# saving the text file
def saveFile():
    file = open("studentMarks.txt", "w")
    file.write(str(len(students)) + "\n")

    for student in students:
        file.write(",".join(student) + "\n")

    file.close()


# entering student details
def studentDetails():
    number = simpledialog.askinteger("Student", "Student number:", minvalue=1000, maxvalue=9999)
    name = simpledialog.askstring("Student", "Student name:")
    mark1 = simpledialog.askinteger("Student", "Coursework 1:", minvalue=0, maxvalue=20)
    mark2 = simpledialog.askinteger("Student", "Coursework 2:", minvalue=0, maxvalue=20)
    mark3 = simpledialog.askinteger("Student", "Coursework 3:", minvalue=0, maxvalue=20)
    exam = simpledialog.askinteger("Student", "Exam mark:", minvalue=0, maxvalue=100)

    if None in [number, name, mark1, mark2, mark3, exam]:
        return None

    if name.strip() == "" or "," in name:
        return None

    return [str(number), name, str(mark1), str(mark2), str(mark3), str(exam)]


# adding a student
def addStudent():
    student = studentDetails()

    if student != None:
        for existing in students:
            if existing[0] == student[0]:
                output.delete("1.0", END)
                output.insert(END, "Student number already exists")
                return

        students.append(student)
        saveFile()
        viewAll()


# deleting a student
def deleteStudent():
    student = findStudent()

    if student != None:
        students.remove(student)
        saveFile()
        viewAll()


# updating a student record
def updateStudent():
    student = findStudent()

    if student != None:
        newStudent = studentDetails()

        if newStudent != None:
            for existing in students:
                if existing != student and existing[0] == newStudent[0]:
                    output.delete("1.0", END)
                    output.insert(END, "Student number already exists")
                    return

            index = students.index(student)
            students[index] = newStudent
            saveFile()
            viewAll()


# creating the window
root = Tk()
root.title("Student Manager")
root.geometry("800x600")
root.config(bg="#101827")


# creating the title
Label(root, text="Student Manager", font=("Arial", 25, "bold"),bg="#101827", fg="white").pack(pady=20)


# creating the menu
menu = Frame(root, bg="#312B85")
menu.pack(pady=10)

Button(menu, text="All Students", width=18, command=viewAll,bg="#5A2380", fg="white").grid(row=0, column=0, padx=5, pady=5)

Button(menu, text="Find Student", width=18, command=viewIndividual,bg="#5A2380", fg="white").grid(row=0, column=1, padx=5, pady=5)

Button(menu, text="Highest Score", width=18, command=highestScore,bg="#5A2380", fg="white").grid(row=0, column=2, padx=5, pady=5)

Button(menu, text="Lowest Score", width=18, command=lowestScore,bg="#5A2380", fg="white").grid(row=0, column=3, padx=5, pady=5)

Button(menu, text="Sort Records", width=18, command=sortRecords,bg="#5A2380", fg="white").grid(row=1, column=0, padx=5, pady=5)

Button(menu, text="Add Student", width=18, command=addStudent,bg="#5A2380", fg="white").grid(row=1, column=1, padx=5, pady=5)

Button(menu, text="Delete Student", width=18, command=deleteStudent,bg="#9F3444", fg="white").grid(row=1, column=2, padx=5, pady=5)

Button(menu, text="Update Student", width=18, command=updateStudent,bg="#5A2380", fg="white").grid(row=1, column=3, padx=5, pady=5)


# creating the output box
output = Text(root, width=80, height=20, font=("Arial", 12),bg="#5A2380", fg="white")

output.pack(padx=20, pady=15, fill=BOTH, expand=True)


# creating the quit button
Button(root, text="Quit", width=15, command=root.destroy,bg="red", fg="white").pack(pady=10)

viewAll()

root.mainloop()

#imports the libraries
from tkinter import *
import random


# defining function to swap frames

def switch_to_frame(frame):
    frame.tkraise()


def displayMenu():
    switch_to_frame(frame1)

#selecting difficulty mode
def randomInt():
    if level == "Easy":
        return random.randint(1, 9)
    elif level == "Medium":
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

#addition and subtraction questions
def decideOperation():
    return random.choice(["+", "-"])


def startQuiz(difficulty):
    global score, question, attempt, level

    score = 0
    question = 0
    attempt = 1
    level = difficulty

    welcome.config(text="Welcome to " + level + " Mode!")
    switch_to_frame(frame2)
    displayProblem()

#displays random addition and subtraction questions
def displayProblem():
    global answer, attempt, question

    if question == 10:
        displayResults()
    else:
        attempt = 1

        num1 = randomInt()
        num2 = randomInt()
        operation = decideOperation()

        if operation == "+":
            answer = num1 + num2
        else:
            answer = num1 - num2

        question_label.config(
            text=str(num1) + " " + operation + " " + str(num2) + " ="
        )

        question_number.config(text="Question " + str(question + 1) + "/10")
        entry.delete(0, END)
        feedback.config(text="")


#if the answer is correct points are awarded
def isCorrect():
    global score, attempt, question

    if entry.get().lstrip("-").isdigit():
        user_answer = int(entry.get())

        if user_answer == answer:

            if attempt == 1:
                score = score + 10
                feedback.config(text="Correct! +10")
            else:
                score = score + 5
                feedback.config(text="Correct! +5")

            question = question + 1
            root.after(1000, displayProblem)

        else:

            if attempt == 1:
                attempt = 2
                feedback.config(text="Wrong! Try again")
                entry.delete(0, END)

            else:
                feedback.config(text="Wrong! Next question")
                question = question + 1
                root.after(1000, displayProblem)

    else:
        feedback.config(text="Enter a number")

#results
def displayResults():
    switch_to_frame(frame3)

    result.config(text="Score: " + str(score) + "/100")

    if score >= 90:
        rank.config(text="Rank: A")
    elif score >= 80:
        rank.config(text="Rank: B")
    elif score >= 70:
        rank.config(text="Rank: C")
    elif score >= 60:
        rank.config(text="Rank: D")
    else:
        rank.config(text="Better luck next time")

#to play the quiz again
def playAgain():
    displayMenu()


# main window

root = Tk()
root.title("Math Quiz")
root.geometry("400x400")
root.config(bg="White")
root.resizable(0, 0)


# frames

frame1 = Frame(root, bg="#542367")
frame2 = Frame(root, bg="#542367")
frame3 = Frame(root, bg="#542367")

frame1.place(x=0, y=0, width=400, height=400)
frame2.place(x=0, y=0, width=400, height=400)
frame3.place(x=0, y=0, width=400, height=400)


# frame 1 difficulty menu

label1 = Label(frame1, text="DIFFICULTY LEVEL",font=("Roboto", 18), bg="#542367", fg="white")
label1.pack(pady=30)

button1 = Button(frame1, text="Easy", command=lambda: startQuiz("Easy"), width=20)
button1.pack(pady=10)

button2 = Button(frame1, text="Medium", command=lambda: startQuiz("Medium"), width=20)
button2.pack(pady=10)

button3 = Button(frame1, text="Hard", command=lambda: startQuiz("Hard"), width=20)
button3.pack(pady=10)


# frame 2 quiz

welcome = Label(frame2, text="", font=("Roboto", 16),bg="#542367", fg="white")
welcome.pack(pady=15)

question_number = Label(frame2, text="", bg="#542367", fg="white")
question_number.pack(pady=10)

question_label = Label(frame2, text="", font=("Roboto", 24),bg="#542367", fg="white")
question_label.pack(pady=15)

entry = Entry(frame2, font=("Roboto", 16), justify="center")
entry.pack(pady=10)

submit = Button(frame2, text="Submit", command=isCorrect)
submit.pack(pady=10)

feedback = Label(frame2, text="", bg="#542367", fg="white")
feedback.pack(pady=10)


# frame 3 results

result = Label(frame3, text="", font=("Roboto", 18),bg="#542367", fg="white")
result.pack(pady=50)

rank = Label(frame3, text="", font=("Roboto", 16),bg="#542367", fg="white")
rank.pack(pady=10)

again = Button(frame3, text="Play Again", command=playAgain)
again.pack(pady=15)

exit_button = Button(frame3, text="Exit", command=root.destroy)
exit_button.pack(pady=5)



#to display and run everything

displayMenu()

root.mainloop()

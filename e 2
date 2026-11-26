
from tkinter import *
import random

#creating function global allows other functions to acess the punchline

def tellJoke():
    global punchline
    joke = random.choice(jokes)
    setup, punchline = joke.split("?", 1)
    setupLabel.config(text=setup + "?")
    punchlineLabel.config(text="")


def showPunchline():
    punchlineLabel.config(text=punchline)


def nextJoke():
    tellJoke()


#reading jokes from the textfile

file = open("randomJokes.txt", "r", encoding="utf-8")
jokes = file.readlines()
file.close()

punchline = ""

#creating window to run the file

root = Tk()
root.title("Joke Assistant")
root.geometry("500x400")
root.config(bg="lightblue")

#title

titleLabel = Label(root, text="Alexa Joke Assistant",font=("Arial", 18),bg="lightblue")
titleLabel.pack(pady=30)

# start up button to click for a joke

setupLabel = Label(root, text="Click the button for a joke!",font=("Arial", 12),bg="lightblue",wraplength=450)
setupLabel.pack(pady=10)

# punchline label

punchlineLabel = Label(root, text="",font=("Arial", 12),bg="lightblue",wraplength=450)
punchlineLabel.pack(pady=20)

# buttons to press

button1 = Button(root, text="Alexa tell me a Joke",command=tellJoke)
button1.pack(pady=5)

button2 = Button(root, text="Show Punchline",command=showPunchline)
button2.pack(pady=5)

button3 = Button(root, text="Next Joke",command=nextJoke)
button3.pack(pady=5)

button4 = Button(root, text="Quit",command=root.destroy)
button4.pack(pady=5)

#runs the window
root.mainloop()

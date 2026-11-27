from tkinter import *
import random

punchline =""
jokecount = 0

#reading jokes from the file randomjokes
file = open("randomJokes.txt", "r", encoding="utf-8")
jokes = file.readlines()
file.close()

#defining the function to display a rando joke
def tellJoke():
    global punchline,jokecount

    joke = random.choice(jokes)
    setup , punchline = joke.split("?" , 1)

    setupLabel.config(text=setup + "?")
    punchlineLabel.config(text="")
    button2.config(state=NORMAL)

    jokecount = jokecount + 1
    counterLabel.config(text="Jokes told: " + str(jokecount))



#function to display the punchline
def showPunchline():
    punchlineLabel.config(text=punchline)
    button2.config(state=DISABLED)

#creating the window
root = Tk()
root.title("joke assistant")
root.geometry("500x500")
root.config(bg="#101C30")

#title
titleLabel = Label(root, text= "Alexa Joke Assistant", font=("Arial" , 22 , "bold"), bg="#101C30", fg="white")
titleLabel.pack(pady=5)

#joke counter
counterLabel = Label(root,text="Jokes told 0", font=("Arial" , 11), bg="#101C30", fg="lightgrey")
counterLabel.pack(pady=5)

#Frame containing the joke
jokeFrame = Frame(root, bg="#22334D")
jokeFrame.pack(padx=25, pady=15, fill="x")

#setup label 
setupLabel = Label(jokeFrame, text="Click the button for a joke!", font=("Arial", 13), bg="#22334D", fg="white", wraplength=400)
setupLabel.pack(pady=20)

#punchline label

punchlineLabel = Label(jokeFrame, text="",font=("Arial", 13, "bold"), bg="#22334D",fg="lightgreen", wraplength=400)
punchlineLabel.pack(pady=15)

# tell joke button
button1 = Button(root, text="Alexa tell me a Joke",command=tellJoke, width=25, bg="#2563EB",fg="white", font=("Arial", 12), relief="flat")
button1.pack(pady=5)

# show punchline button
button2 = Button(root, text="Show Punchline",command=showPunchline, width=25, bg="#334155",fg="white", font=("Arial", 12), relief="flat",state=DISABLED)
button2.pack(pady=5)

# next joke button
button3 = Button(root, text="Next Joke",command=tellJoke, width=25, bg="#334155",fg="white", font=("Arial", 12), relief="flat")
button3.pack(pady=5)

# quit button
button4 = Button(root, text="Quit",command=root.destroy, width=25, bg="#DC2626",fg="white", font=("Arial", 12), relief="flat")
button4.pack(pady=5)

# run the application
root.mainloop()
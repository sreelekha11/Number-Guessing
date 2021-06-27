#Creating a simple GUI Python Guessing Game using Tkinter and getting the computer to choose a random number, check if the user guess is correct and inform the user.

import tkinter
import random

computer_guess = random.randint(1,10)

def Check():
    user_guess = int(number_guess.get())
    
    #Determine higher, lower or correct
    if user_guess < computer_guess:
        msg="Higher!"
    elif user_guess > computer_guess:
        msg="Lower!"
    elif user_guess == computer_guess:
        msg="Correct!"
    else:
        msg="Something went Wrong..."
    #Show the Result
    label_result["text"]= msg

#Create root window
root = tkinter.Tk()
root.title("Number Guessing Game")

#Create Widgets
label_title=tkinter.Label(root, text="Welcome to the Number Guessing Game!")
label_title.pack()

label_result=tkinter.Label(root, text="Good Luck!")
label_result.pack()

button_check=tkinter.Button(root, text="Check", fg="green", command=Check)
button_check.pack(side="left")

button_reset=tkinter.Button(root, text="Reset", fg="red", command=root.quit)
button_reset.pack(side="right")

number_guess=tkinter.Entry(root, width=3)
number_guess.pack()




#Start the main events loop
root.mainloop()



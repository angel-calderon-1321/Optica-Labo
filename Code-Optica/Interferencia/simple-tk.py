#####################
# Program Interference 2024
# by Angel Calderon
#####################
# Clear the terminal screen
from tkinter import *
import os
os.system('clear')
#####################

#####################
# TKinter GUI
#####################

root = Tk() # tkinter obejet
root.title("Hello tk")
root.geometry("800x600")

def myFunction():
    otherLabel = Label(root, text = "Hola "+myTextbox.get()+", como estas.")
    otherLabel.pack()

myLabel = Label(root, text = "Ingrese su nombre") #Label text
myLabel.pack()

myTextbox = Entry(root, width=30) #text box input
myTextbox.pack()

myButton = Button(root, text = "yes", command= myFunction) #button
myButton.pack()

root.mainloop() #loop
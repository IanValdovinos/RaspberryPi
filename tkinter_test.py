# Tkinter is a library used to create GUI
from tkinter import *

# Create a new window 
root = Tk()

# Set the dimensions of the new window
root.geometry('800x600')

# Create a canvas widget to draw figures
c = Canvas(root, width=800, height=600)
c.pack() # Makes the canvas appear 
r = c.create_rectangle(0, 0, 50, 50, fill='blue', outline='red') # Draws a rectangle





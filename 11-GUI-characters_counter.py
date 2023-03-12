# Import the required libraries
from tkinter import *
# Create an instance of tkinter frame or window
win=Tk()
# Set the size of the tkinter window
win.title("Characters Counter")
win.geometry("700x350")
#Ask users to write text
label2=Label(text="Please, write some text", justify=RIGHT, font=('11'))
label2.pack()
# Define a function to get the length of the current text
def update(event):
   label.config(text="Total Characters: "+str(len(text.get("1.0", 'end-1c'))))

# Create a text widget
text=Text(win, width=50, height=10, font=('Calibri 14'))
text.pack()

# Create a Label widget
label=Label(win, text="", justify=CENTER, font=('11'))
label.pack()


# Bind the buttons with the event
text.bind('<KeyPress>', update)
text.bind('<KeyRelease>', update)

win.mainloop()

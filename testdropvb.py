# Import module
from tkinter import *
from tkinter import messagebox

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def show():
    keuze = clicked.get()
    if keuze == "Optie a":
        print("Optie a gekozen")
    elif keuze == "Optie b":
        print("Optie b gekozen")
    else:
        print("Optie c gekozen")
    messagebox.showinfo("Gemaakte keuze",keuze)


# Dropdown menu options
options = [
    "Optie a",
    "Optie b",
    "Optie c"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Maak je keuze" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()

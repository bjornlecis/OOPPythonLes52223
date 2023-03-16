import tkinter as tk

root = tk.Tk()
naam = tk.Label(root, text="Hallo ") #aanmaken van een label
naam.pack() #label toevoegen aan het scherm
i_naam = tk.Entry(root)
i_naam.pack()

root.mainloop()

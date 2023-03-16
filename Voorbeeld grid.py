import tkinter as tk
from tkinter import messagebox

def klik():

    messagebox.askyesno("Vraag","Ben je zeker")

root = tk.Tk()
l_voornaam = tk.Label(root,text="Voornaam").grid(row =0,column =0)
l_achternaam = tk.Label(root,text="Achternaam").grid(row =1,column =0)
i_voornaam = tk.Entry(root,text="s_voornaam").grid(row = 0, column =1)
i_achternaam = tk.Entry(root).grid(row =1, column=1)
btn_bevestig = tk.Button(root,text="bevestig",command=klik).grid(row =2, column =0)
l_resultaat = tk.Label(root,text="*****").grid(row = 3)
root.mainloop()



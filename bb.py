from tkinter import *
import os
root = Tk()
theLabel = Label(root, text="Folow the putun please")
theLabel.pack()

photo = PhotoImage(file="ind.png")
label=Label(root, image=photo)
label.pack()

root.mainloop()

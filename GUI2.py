from tkinter import *
import os
import subprocess

root = Tk()
theLabel = Label(root, text="Folow the putun please")
theLabel.pack()
top= Frame(root)
top.pack()
bottomFrame =Label(root)
bottomFrame.pack(side=BOTTOM)
photo=PhotoImage(file="ind.png")
theLabel=Label(root, image=photo)
theLabel.pack()
def list ():
    exec= "services.msc"
  # subprocess
    os.system(exec)
button1=Button(top, text="Record" , fg="red" , command=list)
button2=Button(top, text="press to enter the name of butun" , fg="blue",command=photo)
button3=Button(bottomFrame, text="end Record" , fg="green" ,command=bottomFrame.quit)
button1.pack()
button2.pack()
button3.pack()
root.mainloop()
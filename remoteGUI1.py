from tkinter import *

root = Tk()
theLabel = Label(root, text="Folow the putun please")
theLabel.pack()
top= Frame(root)
top.pack()


def list ():
    print("irrecord -f -d /dev/lirc0 ~/lirc.conf")


button1=Button(top, text="Record" , fg="red" , command=list)
button2=Button(top, text="press to enter the name of butun" , fg="blue")
# button3=Button(bottomFrame, text="end Record" , fg="green" ,command=frame.quit)
button1.pack()
button2.pack()
# button3.pack()







root.mainloop()

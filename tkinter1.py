from tkinter import *
import os
import subprocess
import random
import time

#pygame.image.load("index.jpg")
root = Tk()
root.geometry("200x650+500+0")
root.resizable(0,0)
theLabel = Label(root, text="Folow the putun please")
theLabel.pack()
top= Frame(root ,widt=500 , height=600)
top.pack()
top2=Frame(root ,widt=500 , height=600)
top2.pack()
top3= Frame(root ,widt=500 , height=600)
top3.pack()
top4= Frame(root ,widt=500 , height=600)
top4.pack()
top5= Frame(root ,widt=500 , height=600)
top5.pack()
top6= Frame(root ,widt=500 , height=600)
top6.pack()
top7= Frame(root ,widt=500 , height=600)
top7.pack()
top8= Frame(root ,widt=500 , height=600)
top8.pack()
top9= Frame(root ,widt=500 , height=600)
top9.pack()
top10= Frame(root ,widt=500 , height=600)
top10.pack()
top11= Frame(root ,widt=500 , height=600)
top11.pack()


def thre():
    exec = "KEY_3"
    # subprocess
    os.system(exec)


def one():
    exec = "KEY_1"
    # subprocess
    os.system(exec)


def two():
    exec = "KEY_2"
    # subprocess
    os.system(exec)


bottomFrame =Label(root)
bottomFrame.pack(side=BOTTOM)
photo=PhotoImage(file="ind.png")
theLabel=Label(root, image=photo)
theLabel.pack()
def stop ():
    exec= "sudo /etc/init.d/lircd stop"
  # subprocess
    os.system(exec)

def list ():
    exec= "services.msc"
  # subprocess
    os.system(exec)




button1=Button(top, text="Record" , fg="red" , command=list)
button2=Button(top2, text="Power" , fg="red" )
button3=Button(top2, text="Silnce" , fg="red")
button4=Button(top3, text="1" , fg="red" ,command=one)
button5=Button(top3, text="2" , fg="red" ,command=two)
button6=Button(top3, text="3" , fg="red" ,command=thre)
button7=Button(top4, text="4" , fg="red")
button8=Button(top4, text="5" , fg="red")
button9=Button(top4, text="6" , fg="red")
button10=Button(top5, text="7" , fg="red")
button11=Button(top5, text="8" , fg="red")
button12=Button(top5, text="9" , fg="red")
button13=Button(top6, text="0" , fg="red")
button14=Button(top7, text="up" , fg="red")
button15=Button(top9, text="down" , fg="red")
button16=Button(top8, text="left" , fg="red")
button17=Button(top8, text="right" , fg="red")
button18=Button(top8, text="OK" , fg="red")
button19=Button(top10, text="MENU" , fg="red")
button20=Button(top10, text="EXIT" , fg="red")
button23=Button(top11, text="BACK" , fg="red")

button21=Button(bottomFrame, text="chek befor recording" , fg="blue",command=stop)
button22=Button(bottomFrame, text="end Record" , fg="green" ,command=bottomFrame.quit)
button1.pack(side= LEFT)
button2.pack( side= RIGHT)
button3.pack(side= LEFT)
button4.pack(side= LEFT )
button5.pack(side= LEFT)
button6.pack(side= LEFT)
button7.pack(side= LEFT)
button8.pack(side= LEFT)
button9.pack(side= LEFT)
button10.pack(side= LEFT)
button11.pack(side= LEFT)
button12.pack(side= LEFT)
button13.pack(side= RIGHT)
button14.pack(side= RIGHT)
button15.pack(side= RIGHT)
button16.pack(side= RIGHT)
button17.pack(side= RIGHT)
button18.pack(side= RIGHT)
button19.pack(side= RIGHT)
button20.pack(side= RIGHT)
button21.pack()
button22.pack()
button23.pack()

root.mainloop()

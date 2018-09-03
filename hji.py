from tkinter import *
from pynput.keyboard import *
import time
import tkinter.messagebox
import remoteGUI


keyboard = Controller()

def stop ():
    # exec= "sudo /etc/init.d/lircd stop"
  # subprocess
    if __name__ == '__main__':
        remoteGUI

    # os.system(exec)


def list ():
    exec1= "services.msc"
  # subprocess
    os.system(exec1)
    root = Tk()
    tkinter.messagebox._show('Reccording',"the record of your remote is completed ")
    root.mainloop()
def main():
    window = Tk()
    window.title('Remote Ccntrol')
    window.geometry("450x150+500+100")
    window.resizable(0, 0)
    window.configure(background='grey83')

    #Menu Bar
    menubar = Menu(window)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer")
    menu1.add_command(label="Editer")
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=window.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Editer", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu3)

    window.config(menu=menubar)


    MainFrame = Frame(window,bg='grey83')
    MainFrame.grid(row=0,column=0,padx=8,pady=8)
    lab1=Label(MainFrame,text="device_name", width=15, height=1, bg='grey83', fg='white')
    lab1.grid(row=1 , sticky=E)
    en1=Entry(MainFrame)
    en2 = Entry(MainFrame)

    lab2 = Label(MainFrame, text="device_type", width=15, height=1, bg='grey83', fg='white')
    lab2.grid(row=3, sticky=E)
    en1.grid(row=1,column=1)
    en2.grid(row=3, column=1)
    bp=tkinter.messagebox.INFO

    #Row One

    buttonOnOff = Button(MainFrame, text='Record', width=15, height=2, bg='red2', fg='white' ,command=list )
    buttonOnOff.grid(row=0, column=0, padx=5, pady=5)

    # buttonMedia = Button(MainFrame, text='Menu', width=15, height=2, bg='grey45', fg='white')
    # buttonMedia.grid(row=0, column=2, padx=5, pady=5)

    buttonSound = Button(MainFrame, text='Stop', width=15, height=2, fg='white',bg='green3' ,command=stop)
    buttonSound.grid(row=0, column=3, padx=5, pady=5)




    window.mainloop()

if __name__ == '__main__':
    main()
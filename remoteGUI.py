from tkinter import *
from pynput.keyboard import *
import time


keyboard = Controller()
def main():
    window = Tk()
    window.title('Remote Ccntrol')
    window.geometry("500x500+500+100")
    window.resizable(0, 0)
    window.configure(background='grey10')

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


    MainFrame = Frame(window,bg='grey10')
    MainFrame.grid(row=0,column=0,padx=8,pady=8)

    #Row One
    buttonOnOff = Button(MainFrame, text='POWER', width=15, height=2, bg='red2', fg='white' ,command=power)
    buttonOnOff.grid(row=0, column=0, padx=5, pady=5)

    # buttonMedia = Button(MainFrame, text='Menu', width=15, height=2, bg='grey45', fg='white')
    # buttonMedia.grid(row=0, column=2, padx=5, pady=5)

    buttonSound = Button(MainFrame, text='Sound', width=15, height=2, fg='white',bg='green3',command=sound)
    buttonSound.grid(row=0, column=3, padx=5, pady=5)


    #Row Two

    buttonMenu = Button(MainFrame, text='Menu', width=15, height=2, bg='grey45',fg='white' ,command=menu)
    buttonMenu.grid(row=1, column=2, padx=5, pady=5)

    #Row Three
    button1 = Button(MainFrame, text='1', width=15, height=2, fg='white', bg='grey45',command=one)
    button1.grid(row=2, column=0, padx=5, pady=5)

    button2 = Button(MainFrame, text='2', width=15, height=2, bg='grey45', fg='white',command=two)
    button2.grid(row=2, column=2, padx=5, pady=5)

    button3 = Button(MainFrame, text='3', width=15, height=2, bg='grey45', fg='white',command=three)
    button3.grid(row=2, column=3, padx=5, pady=5)

    # Row Four
    button4 = Button(MainFrame, text='4', width=15, height=2, bg='grey45', fg='white',command=four)
    button4.grid(row=3, column=0, padx=5, pady=5)

    button5 = Button(MainFrame, text='5', width=15, height=2, bg='grey45', fg='white',command=five)
    button5.grid(row=3, column=2, padx=5, pady=5)

    button6 = Button(MainFrame, text='6', width=15, height=2, bg='grey45', fg='white',command=six)
    button6.grid(row=3, column=3, padx=5, pady=5)

    # Row Five
    button7 = Button(MainFrame, text='7', width=15, height=2, bg='grey45', fg='white',command=seven)
    button7.grid(row=4, column=0, padx=5, pady=5)

    button8 = Button(MainFrame, text='8', width=15, height=2, bg='grey45', fg='white',command=eight)
    button8.grid(row=4, column=2, padx=5, pady=5)

    button9 = Button(MainFrame, text='9', width=15, height=2, bg='grey45', fg='white',command=nine)
    button9.grid(row=4, column=3, padx=5, pady=5)

    # Row Six
    buttonBack = Button(MainFrame, text='Back', width=15, height=2, bg='grey45', fg='white',command=back)
    buttonBack.grid(row=5, column=0, padx=5, pady=5)

    button0 = Button(MainFrame, text='0', width=15, height=2, bg='grey45', fg='white',command=zero)
    button0.grid(row=5, column=2, padx=5, pady=5)

    buttonExit = Button(MainFrame, text='Exit', width=15, height=2, bg='grey45', fg='white',command=exit)
    buttonExit.grid(row=5, column=3, padx=5, pady=5)

    # Row Seven
    buttonVolUp = Button(MainFrame, text='VOL+', width=15, height=2, bg='medium turquoise', fg='black',command=volup)
    buttonVolUp.grid(row=6, column=0, padx=5, pady=5)

    buttonOk = Button(MainFrame, text='OK', width=15, height=2, bg='grey45', fg='white',command=ok)
    buttonOk.grid(row=6, column=2, padx=5, pady=5)

    buttonDown = Button(MainFrame, text='VOL-', width=15, height=2, bg='medium turquoise', fg='black',command=voldown)
    buttonDown.grid(row=6, column=3, padx=5, pady=5)

    # Row Eight
    buttonUp = Button(MainFrame, text='Up', width=15, height=2, bg='medium turquoise', fg='black',command=up)
    buttonUp.grid(row=7, column=0, padx=5, pady=5)

    buttonTools = Button(MainFrame, text='Tools', width=15, height=2, bg='grey45', fg='red',command=tools)
    buttonTools.grid(row=7, column=2, padx=5, pady=5)

    buttonDown = Button(MainFrame, text='Down', width=15, height=2, bg='medium turquoise', fg='black',command=down)
    buttonDown.grid(row=7, column=3, padx=5, pady=5)

    # Row 9
    buttonLeft = Button(MainFrame, text='Left', width=15, height=2, bg='medium turquoise', fg='black',command=left)
    buttonLeft.grid(row=8, column=0, padx=5, pady=5)

    buttonFav = Button(MainFrame, text='Fav', width=15, height=2, bg='grey45', fg='black',command=fav)
    buttonFav.grid(row=8, column=2, padx=5, pady=5)

    buttonRight = Button(MainFrame, text='Right', width=15, height=2, bg='medium turquoise', fg='black',command=right)
    buttonRight.grid(row=8, column=3, padx=5, pady=5)

    window.mainloop()
def power ():
    time.sleep(2)
    keyboard.type("KEY_POWER")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def menu ():
    time.sleep(2)
    keyboard.type("KEY_MENU")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def zero ():
    time.sleep(2)
    keyboard.type("KEY_0")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def one ():
    time.sleep(2)
    keyboard.type("KEY_1")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def  two ():
    time.sleep(2)
    keyboard.type("KEY_2")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def three ():
    time.sleep(2)
    keyboard.type("KEY_3")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def four ():
    time.sleep(2)
    keyboard.type("KEY_4")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def five ():
    time.sleep(2)
    keyboard.type("KEY_5")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def six ():
    time.sleep(2)
    keyboard.type("KEY_6")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def seven ():
    time.sleep(2)
    keyboard.type("KEY_7")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def eight ():
    time.sleep(2)
    keyboard.type("KEY_8")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def nine ():
    time.sleep(2)
    keyboard.type("KEY_9")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def fav ():
    time.sleep(2)
    keyboard.type("KEY_FAVORITES")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def sound ():
    time.sleep(2)
    keyboard.type("KEY_SOUND")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def ok ():
    time.sleep(2)
    keyboard.type("KEY_OK")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def home ():
    time.sleep(2)
    keyboard.type("KEY_HOME")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def back ():
    time.sleep(2)
    keyboard.type("KEY_BACK")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def volup ():
    time.sleep(2)
    keyboard.type("KEY_VOLUMEUP")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def voldown ():
    time.sleep(2)
    keyboard.type("KEY_VOLUMEDOWN")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def up ():
    time.sleep(2)
    keyboard.type("KEY_UP")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def down ():
    time.sleep(2)
    keyboard.type("KEY_DOWN")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def right ():
    time.sleep(2)
    keyboard.type("KEY_RIGHT")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def left ():
    time.sleep(2)
    keyboard.type("KEY_LEFT")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def exit ():
    time.sleep(2)
    keyboard.type("KEY_END")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
def tools ():
    time.sleep(2)
    keyboard.type("KEY_SETUP")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

if __name__ == '__main__':
    main()
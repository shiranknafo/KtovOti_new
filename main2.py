from tkinter import *

from KtovOti_new import writing_letter
from writing_letter import *
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox
from random import randint


def myWindow1():
    window = Tk()
    window.title("KTOVOTI")
    window.config(bg='white')
    window.geometry('640x480')

    canvas1 = Canvas(window, bg='white', width=400, height=300, relief='raised')
    canvas1.pack()

    label1 = Label(window, text='ברוכים הבאים לכתובותי')
    label1.config(font=('helvetica', 20, 'bold'))
    canvas1.create_window(200, 25, window=label1)

    label2 = Label(window, text=':בחר שיעור')
    label2.config(font=('helvetica', 15))
    canvas1.create_window(200, 100, window=label2)


    def writing_class():
        new_window = Toplevel(window)  # Create a new window
        new_window.title("כתיבה")
        new_window.geometry("250x150")
        l = writing_letter.get_letter()
        Label(new_window, text=":תכתוב את האות הבאה").pack(pady=20)
        label1 = Label(new_window, text=l, font=('helvetica', 15, 'bold'))
        label1.pack()
        #com = writing_letter.compare_images()
        #if com:
         #   label4 = Label(new_window, text="כל הכבוד", font=('helvetica', 15, 'bold'))
        button = Button(new_window , text='הבא', command = (new_window.destroy, writing_class)).pack(pady=20)

        button2 = Button(new_window , text='תפריט', command = new_window.destroy).pack(pady=20)


    button1 = Button(text='שמע', command = writing_class, bg='brown', fg='white',
                             font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)

    window.mainloop()


myWindow1()
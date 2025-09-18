

from KtovOti_new import writing_letter
from KtovOti_new import sound_letter
from tkinter import messagebox
from tkinter import *
import pygame
import consts
import random
import random_letter_sound
import tkinter.messagebox


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
        button = Button(new_window, text='הבא', command=(writing_class)).pack(pady=20)
        buttonmenu = Button(new_window, text='תפריט', command=new_window.destroy).pack(pady=20)
        from KtovOti_new import save_image_try
        com = writing_letter.compare_images(l)
        if writing_letter.compare_images(l):
            messagebox.showinfo("כל הכבוד!", "תשובה נכונה")
        else:
            messagebox.showinfo("בוז!", "בוז!")

    def play_game():
        main_sound, main_letter, main_options = sound_letter.choose_sound()

        root = Tk()

        root.minsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)
        root.maxsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)

        sound_frame = Frame(root)
        sound_frame.pack(side=TOP, padx=50, pady=50)

        answer_frame = Frame(root)
        answer_frame.pack(side=TOP, padx=50, pady=50)

        pygame.mixer.init()

        def start():
            temp = main_options.copy()
            for i in range(4):
                letter = random.choice(temp)
                temp.remove(letter)
                if i == 0:
                    btn_text1.set(letter)
                elif i == 1:
                    btn_text2.set(letter)
                elif i == 2:
                    btn_text3.set(letter)
                else:
                    btn_text4.set(letter)

        def play_sound():
            pygame.mixer.music.load(main_sound)
            pygame.mixer.music.play(loops=0)

        def check_answer(text):
            if text == main_letter:
                tkinter.messagebox.showinfo("כל הכבוד!", "תשובה נכונה")  # ok
            else:
                tkinter.messagebox.showinfo("איזה באסה", f"תשובה לא נכונה. התשובה הנכונה:\n {sound_letter.LETTER}")  # ok

        def answer_1(event):
            check_answer(btn_text1.get())

        def answer_2(event):
            check_answer(btn_text2.get())

        def answer_3(event):
            check_answer(btn_text3.get())

        def answer_4(event):
            check_answer(btn_text4.get())

        btn_start = Button(sound_frame, text=":שחק", command=start)
        btn_start.config(font=("Courier", 15), fg="black", bg="purple")
        btn_start.pack(side=TOP)

        sound_label = Label(sound_frame, text=" :איזה אות עושה את הצליל ")
        sound_label.config(font=("Courier", 25))
        sound_label.pack(side=TOP)
        sound_label.pack(side=RIGHT)
        play_button = Button(sound_frame, text="הפעל", command=play_sound)
        play_button.config(font=("Courier", 25), fg="black", bg="lightblue")
        play_button.pack(side=RIGHT)

        btn_text1 = StringVar()
        letter1 = Button(answer_frame, textvariable=btn_text1)
        letter1.bind("<Button-1>", answer_1)
        letter1.config(font=("Courier", 40), fg="black", bg="pink")
        letter1.grid(row=0, column=0)

        btn_text2 = StringVar()
        letter2 = Button(answer_frame, textvariable=btn_text2)
        letter2.bind("<Button-1>", answer_2)
        letter2.config(font=("Courier", 40), fg="black", bg="pink")
        letter2.grid(row=0, column=1)

        btn_text3 = StringVar()
        letter3 = Button(answer_frame, textvariable=btn_text3)
        letter3.bind("<Button-1>", answer_3)
        letter3.config(font=("Courier", 40), fg="black", bg="pink")
        letter3.grid(row=0, column=2)

        btn_text4 = StringVar()
        letter4 = Button(answer_frame, textvariable=btn_text4)
        letter4.bind("<Button-1>", answer_4)
        letter4.config(font=("Courier", 40), fg="black", bg="pink")
        letter4.grid(row=0, column=3)



    button1 = Button(window, text='כתיבה', command = writing_class, bg='pink', fg='black',
                             font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=button1)
    button2 = Button(window, text='שמע',command= play_game, bg='pink', fg='black',
                    font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 280, window=button2)

    window.mainloop()


myWindow1()
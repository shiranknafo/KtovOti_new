from tkinter import *
import pygame
import consts
import random
import random_letter_sound
import tkinter.messagebox




SOUND, LETTER, OPTIONS = random_letter_sound.choose_sound()

root = Tk()

root.minsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)
root.maxsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)

sound_frame = Frame(root)
sound_frame.pack(side=TOP, padx=50, pady=50)

answer_frame = Frame(root)
answer_frame.pack(side=TOP, padx=50, pady=50)

pygame.mixer.init()

def start():
    temp = OPTIONS.copy()
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
    pygame.mixer.music.load(SOUND)
    pygame.mixer.music.play(loops=0)

def check_answer(text):
    if text == LETTER:
        tkinter.messagebox.showinfo("כל הכבוד!", "תשובה נכונה")  # ok
    else:
        tkinter.messagebox.showinfo("איזה באסה", f"תשובה לא נכונה. התשובה הנכונה:\n {LETTER}")  # ok

def answer_1(event):
    print(btn_text1.get())
    check_answer(btn_text1.get())

def answer_2(event):
    print(btn_text2.get())
    check_answer(btn_text2.get())

def answer_3(event):
    print(btn_text3.get())
    check_answer(btn_text3.get())

def answer_4(event):
    print(btn_text4.get())
    check_answer(btn_text4.get())

btn_start = Button(sound_frame, text=":שחק",command=start)
btn_start.config(font=("Courier", 15),fg="black",bg="green")
btn_start.pack(side=TOP)

sound_label = Label(sound_frame, text=" :איזה אות עושה את הצליל ")
sound_label.config(font=("Courier", 25))
sound_label.pack(side=TOP)
sound_label.pack(side=RIGHT)
play_button = Button(sound_frame, text="הפעל",command=play_sound)
play_button.config(font=("Courier", 25),fg="black",bg="yellow")
play_button.pack(side=RIGHT)

btn_text1 = StringVar()
letter1 = Button(answer_frame, textvariable=btn_text1)
letter1.bind("<Button-1>", answer_1)
letter1.config(font=("Courier", 40),fg="black",bg="lightblue")
letter1.grid(row=0, column=0)

btn_text2 = StringVar()
letter2 = Button(answer_frame, textvariable=btn_text2)
letter2.bind("<Button-1>", answer_2)
letter2.config(font=("Courier", 40),fg="black",bg="lightblue")
letter2.grid(row=0, column=1)

btn_text3 = StringVar()
letter3 = Button(answer_frame, textvariable=btn_text3)
letter3.bind("<Button-1>", answer_3)
letter3.config(font=("Courier", 40),fg="black",bg="lightblue")
letter3.grid(row=0, column=2)

btn_text4 = StringVar()
letter4 = Button(answer_frame, textvariable=btn_text4)
letter4.bind("<Button-1>", answer_4)
letter4.config(font=("Courier", 40),fg="black",bg="lightblue")
letter4.grid(row=0, column=3)

root.mainloop()\

from KtovOti_new import writing_letter
from tkinter import messagebox
from tkinter import *
import pygame
import consts
import random
import random_letter_sound
import tkinter.messagebox

def choose_sound():
    letter_sound = random.choice(list(consts.LETTERS_SOUNDS_DICT.items()))
    letter = letter_sound[0]
    sound = letter_sound[1]
    options = answer_options(letter)
    options.append(letter)
    return sound, letter, options


def answer_options(letter):
    temp = []  ##add checks
    for item in consts.LETTERS_SOUNDS_DICT.items():
        if letter != item[0]:
            temp.append(item[0])
    options = random.sample(temp, 3)
    return options


def play_game():
    main_sound, main_letter, main_options = choose_sound()

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
            tkinter.messagebox.showinfo("איזה באסה", f"תשובה לא נכונה. התשובה הנכונה:\n {LETTER}")  # ok

    def answer_1(event):
        check_answer(btn_text1.get())

    def answer_2(event):
        check_answer(btn_text2.get())

    def answer_3(event):
        check_answer(btn_text3.get())

    def answer_4(event):
        check_answer(btn_text4.get())

    btn_start = Button(sound_frame, text=":שחק", command=start)
    btn_start.config(font=("Courier", 15), fg="black", bg="green")
    btn_start.pack(side=TOP)

    sound_label = Label(sound_frame, text=" :איזה אות עושה את הצליל ")
    sound_label.config(font=("Courier", 25))
    sound_label.pack(side=TOP)
    sound_label.pack(side=RIGHT)
    play_button = Button(sound_frame, text="הפעל", command=play_sound)
    play_button.config(font=("Courier", 25), fg="black", bg="yellow")
    play_button.pack(side=RIGHT)

    btn_text1 = StringVar()
    letter1 = Button(answer_frame, textvariable=btn_text1)
    letter1.bind("<Button-1>", answer_1)
    letter1.config(font=("Courier", 40), fg="black", bg="lightblue")
    letter1.grid(row=0, column=0)

    btn_text2 = StringVar()
    letter2 = Button(answer_frame, textvariable=btn_text2)
    letter2.bind("<Button-1>", answer_2)
    letter2.config(font=("Courier", 40), fg="black", bg="lightblue")
    letter2.grid(row=0, column=1)

    btn_text3 = StringVar()
    letter3 = Button(answer_frame, textvariable=btn_text3)
    letter3.bind("<Button-1>", answer_3)
    letter3.config(font=("Courier", 40), fg="black", bg="lightblue")
    letter3.grid(row=0, column=2)

    btn_text4 = StringVar()
    letter4 = Button(answer_frame, textvariable=btn_text4)
    letter4.bind("<Button-1>", answer_4)
    letter4.config(font=("Courier", 40), fg="black", bg="lightblue")
    letter4.grid(row=0, column=3)

    root.mainloop()

play_game()
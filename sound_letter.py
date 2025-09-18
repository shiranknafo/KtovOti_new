from tkinter import *
import pygame
import consts
import random
import random_letter_sound
import tkinter.messagebox

SOUND, LETTER, OPTIONS = random_letter_sound.choose_sound()

root = Tk()

root.geometry(f"{consts.ROOT_HEIGHT}x{consts.ROOT_WIDTH}")
root.minsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)
root.maxsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)

sound_frame = Frame(root)
sound_frame.pack(side=TOP, fill=X)

answer_frame = Frame(root)
answer_frame.pack(side=BOTTOM, fill=X)

pygame.mixer.init()

def choose_sound():
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

sound_label = Label(sound_frame, text="איזה אות עושה את הצליל: ")
sound_label.pack(side=RIGHT)
play_button = Button(sound_frame, text="הפעל",command=choose_sound)
play_button.pack(side=RIGHT)


btn_text1 = StringVar()
letter1 = Button(answer_frame, textvariable=btn_text1)
letter1.bind("<Button-1>", answer_1)
letter1.pack(side=LEFT)
btn_text2 = StringVar()
letter2 = Button(answer_frame, textvariable=btn_text2)
letter2.bind("<Button-1>", answer_2)
letter2.pack(side=LEFT)
btn_text3 = StringVar()
letter3 = Button(answer_frame, textvariable=btn_text3)
letter3.bind("<Button-1>", answer_3)
letter3.pack(side=LEFT)
btn_text4 = StringVar()
letter4 = Button(answer_frame, textvariable=btn_text4)
letter4.bind("<Button-1>", answer_4)
letter4.pack(side=LEFT)



root.mainloop()
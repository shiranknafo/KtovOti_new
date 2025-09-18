from tkinter import *
import pygame

root = Tk()

pygame.mixer.init()
def play(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)

my_button = Button(root, text="Play song",command=play)
my_button.pack()



root.mainloop()
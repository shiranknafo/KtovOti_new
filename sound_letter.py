from tkinter import *
import pygame
import consts

root = Tk()
root.geometry(f"{consts.ROOT_HEIGHT}x{consts.ROOT_WIDTH}")
root.minsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)
root.maxsize(consts.ROOT_HEIGHT, consts.ROOT_WIDTH)
pygame.mixer.init()
# def play(sound):
#     pygame.mixer.music.load(sound)
#     pygame.mixer.music.play(loops=0)
#
# my_button = Button(root, text="Play song",command=play)
# my_button.pack()



root.mainloop()
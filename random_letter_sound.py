# from tkinter import *
# import pygame
# import consts
# import random
#
# def choose_sound():
#     letter_sound = random.choice(list(consts.LETTERS_SOUNDS_DICT.items()))
#     letter = letter_sound[0]
#     sound = letter_sound[1]
#     options = answer_options(letter)
#     options.append(letter)
#     return sound, letter, options
#
# def answer_options(letter):
#     temp = [] ##add checks
#     for item in consts.LETTERS_SOUNDS_DICT.items():
#         if letter != item[0]:
#             temp.append(item[0])
#     options = random.sample(temp, 3)
#     return options
#
#
#

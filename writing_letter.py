import consts
import image_coparison
import string
import random

def get_image(letter):
    return consts.LETTERS_IMAGES_DICT[letter]

def get_letter():
    consts.curr_letter = random.choice(string.ascii_letters)
    return consts.curr_letter

def compare_images(letter):
    letter_image = get_image(letter)
    letter_drawing = 'image.png'
    return image_coparison.compare_two_images(letter_image, letter_drawing)

import consts
import image_coparison
import string
import random

letter = random.choice(string.ascii_letters)

def get_letter():
    return letter

def get_image():
    return consts.ANIMALS_DICT[letter]

def compare_images():
    letter_image = get_image()
    letter_drawing = 'letter_drawing.png'
    return image_coparison.compare_two_images(letter_image, letter_drawing)

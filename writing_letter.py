import consts
import image_coparison
import string
import random

def get_image(letter):
    return consts.LETTERS_IMAGES_DICT[letter]

def get_letter():
    letter = random.choice(string.ascii_letters)
    return letter

def compare_images():
    letter_image = get_image()
    letter_drawing = 'image.png'
    return image_coparison.compare_two_images(letter_image, letter_drawing)

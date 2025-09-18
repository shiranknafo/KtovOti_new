from tkinter import *
from PIL import Image, ImageTk

dict1={ }
img=Image.open("pictures/elefant.png")
img.show()
img=Image.open("pictures/cat.jpg")
img.show()
dict1["e"]=img
dict1["c"]=img
img=Image.open("pictures/lion.png")
dict1["l"]=img
img=Image.open("pictures/dog.png")
dict1["d"]=img
img=Image.open("pictures/monkey.jpg")
dict1["m"]=img
img=Image.open("pictures/bat.png")
dict1["b"]=img
print(dict1)
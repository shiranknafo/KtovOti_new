from PIL import ImageTk, Image,ImageDraw
import PIL
from tkinter import *

width=500
height=500
center=height//2
white=(255,255,255)
green=(0,128,0)

def save():
    file_name="image.png"
    image1.save(file_name)

def paint(event):
    x1,y1=(event.x-1),(event.y-1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1,y1,x2,y2,fill="black",width=5)
    draw.line([x1,y1,x2,y2],fill="black",width=10)

root=Tk()

cv=Canvas(root,width=width,height=height,bg="white")
cv.pack()

image1=PIL.Image.new("RGB",(width,height),white)
draw=ImageDraw.Draw(image1)

cv.pack(expand=YES,fill=BOTH)
cv.bind("<B1-Motion>",paint)

button=Button(root, text="save",command=save)
button.pack()
root.mainloop()

# # from tkinter import *
# # import tkinter.font as tkFont
# #
# #
# #
# # root = Tk()
# # the_label = Label(root, font= ("ariel", 30) , text="Welcome to KtovOti")
# # # the_label =
# # the_label.grid(row=0, column=7)
# #
# # increase_button = Button(root, text="Increase Font Size", command=increase_font_size)
# # increase_button.pack()
# # button1 = Button(root,
# #                    text="Click Me",
# #                    activebackground="light gray",
# #                    activeforeground="white",
# #                    anchor="center",
# #                    bd=3,
# #                    bg="yellow",
# #                    cursor="hand2",
# #                    disabledforeground="yellow",
# #                    fg="black",
# #                    font=("Arial", 12),
# #                    height=2,
# #                    highlightbackground="black",
# #                    highlightcolor="green",
# #                    highlightthickness=2,
# #                    justify="left",
# #                    overrelief="raised",
# #                    padx=10,
# #                    pady=5,
# #                    width=15,
# #                    wraplength=100,
# #                    command = decrease_font_size)
# #
# # button1.grid(row=10, column=10, padx=5, pady=5)
# #
# # button2 = Button(root,
# #                    text="Click Me",
# #                    activebackground="light gray",
# #                    activeforeground="white",
# #                    anchor="center",
# #                    bd=3,
# #                    bg="yellow",
# #                    cursor="hand2",
# #                    disabledforeground="yellow",
# #                    fg="black",
# #                    font=("Arial", 12),
# #                    height=2,
# #                    highlightbackground="black",
# #                    highlightcolor="green",
# #                    highlightthickness=2,
# #                    justify="left",
# #                    overrelief="raised",
# #                    padx=10,
# #                    pady=5,
# #                    width=15,
# #                    wraplength=100)
# #
# # button2.grid(row=10, column=5, padx=5, pady=5)
# #
# # button3 = Button(root,
# #                    text="שמע",
# #                    activebackground="light gray",
# #                    activeforeground="white",
# #                    anchor="center",
# #                    bd=3,
# #                    bg="yellow",
# #                    cursor="hand2",
# #                    disabledforeground="yellow",
# #                    fg="black",
# #                    font=("Arial", 12),
# #                    height=2,
# #                    highlightbackground="black",
# #                    highlightcolor="green",
# #                    highlightthickness=2,
# #                    justify="left",
# #                    overrelief="raised",
# #                    padx=10,
# #                    pady=5,
# #                    width=15,
# #                    wraplength=100)
# #
# # button3.grid(row=15, column=5, padx=5, pady=5)
# # # # root.mainloop()
# # #
# # # top_frame = Frame(root)
# # # top_frame.pack()
# # #
# # # button1 = Button(top_frame,text="Click Me",fg="red")
# # #
# # # button1.pack()
# # #
# # # one = Label(root, text="one",bg="red", fg="white")
# # # one.pack()
# # # two = Label(root, text="two",bg="green", fg="black")
# # # two.pack(fill=X) #fill it as long as the X value is
# # # three = Label(root, text="three",bg="blue", fg="white")
# # # three.pack(side = LEFT , fill=Y) #fill as long as Y value is
# #
# # # root = Tk()
# # # #grid layout - lay out in rows and columns
# # # label_1 = Label(root, text ="name")
# # # label_2 = Label(root, text ="password")
# # # entry_1 = Entry(root) #input
# # # entry_2 = Entry(root)
# # #
# # #
# # # label_1.grid(row=0) #by default columns = 0
# # # # #sticky = align according to N,E,S,W (north-top,east-right,south-bottom,west-left
# # # label_2.grid(row=1)  #under
# # # entry_1.grid(row=0,column=1) #place entry to the right
# # # entry_2.grid(row=1,column=1)
# # #
# # #
# # # #add widget that takes up two columns
# # # c = Checkbutton(root,text="keep me logged in") #true or false if clicked or not
# # # c.grid(columnspan=2)
# #
# #
# #
# # root.mainloop()
#
# from tkinter import *
# from tkinter.ttk import *
#
# # Class for creating a new window
# class NewWindow(Toplevel):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.title("Shema")
#         self.geometry("250x150")
#
#         Label(self, text="This is a new window").pack(pady=20)
#
# # Create the main window
# master = Tk()
# master.geometry("300x200")
# master.title("Main Window")
#
# Label(master, text="This is the main window").pack(pady=10)
#
# # Create a button to open the new window using the class
# btn = Button(master, text="Open New Window")
# btn.bind("<Button>", lambda e: NewWindow(master))  # Bind the event
#
# btn.pack(pady=10)
#
# # Run the Tkinter event loop
# master.mainloop()


import tkinter as tk
from tkinter import colorchooser, Canvas, N
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageGrab
import keyboard


def save(widget, filelocation):
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save(filelocation)


def type_of(color):
    type_pen = 'marker'
    if type_pen == 'marker':
        pencil_motion_marker(color=color)


# pixel pen
def pencil_motion_marker(color):
    stage.bind('<Button-1>', get_pos_marker)
    stage.bind('<B1-Motion>', lambda event, color=color: pencil_draw_marker(event, color))


def get_pos_marker(event):
    global lastx, lasty

    lastx, lasty = event.x, event.y


def pencil_draw_marker(event, color):
    stage.create_line((lastx, lasty, event.x, event.y), width=width.get(), fill=color, capstyle='round')
    get_pos_marker(event)


def choose_pen_color():
    pencilcolor = colorchooser.askcolor(title='Pencil Color')
    type_of(pencilcolor[1])


##

def pencil_click():
    global width, opacity

    Whitepencolb = Button(optionsframe, text='Whitepencolimg', style='COLBG.TButton',
                          command=lambda m='White': type_of(m))
    Whitepencolb.grid(row=0, column=0, padx=10, pady=1)

    Redpencolb = Button(optionsframe, text='Redpencolimg', style='COLBG.TButton', command=lambda m='Red': type_of(m))
    Redpencolb.grid(row=1, column=0, padx=10, pady=1)

    Magentapencolb = Button(optionsframe, text='Magentapencolimg', style='COLBG.TButton',
                            command=lambda m='Magenta': type_of(m))
    Magentapencolb.grid(row=0, column=1, padx=10, pady=1)

    Limegreenpencolb = Button(optionsframe, text='Limegreenpencolimg', style='COLBG.TButton',
                              command=lambda m='Lime': type_of(m))
    Limegreenpencolb.grid(row=1, column=1, padx=10, pady=1)

    Greenpencolb = Button(optionsframe, text='Greenpencolimg', style='COLBG.TButton',
                          command=lambda m='Green': type_of(m))
    Greenpencolb.grid(row=0, column=2, padx=10, pady=1)

    Bluepencolb = Button(optionsframe, text='Bluepencolimg', style='COLBG.TButton', command=lambda m='Blue': type_of(m))
    Bluepencolb.grid(row=1, column=2, padx=10, pady=1)

    Cyanpencolb = Button(optionsframe, text='Cyanpencolimg', style='COLBG.TButton', command=lambda m='Cyan': type_of(m))
    Cyanpencolb.grid(row=0, column=3, padx=10, pady=1)

    Yellowpencolb = Button(optionsframe, text='Yellowpencolimg', style='COLBG.TButton',
                           command=lambda m='Yellow': type_of(m))
    Yellowpencolb.grid(row=1, column=3, padx=10, pady=1)

    Orangepencolb = Button(optionsframe, text='Orangepencolimg', style='COLBG.TButton',
                           command=lambda m='Orange': type_of(m))
    Orangepencolb.grid(row=0, column=4, padx=10, pady=1)

    Graypencolb = Button(optionsframe, text='Graypencolimg', style='COLBG.TButton', command=lambda m='Gray': type_of(m))
    Graypencolb.grid(row=1, column=4, padx=10, pady=1)

    Blackpencolb = Button(optionsframe, text='Blackpencolimg', style='COLBG.TButton',
                          command=lambda m='Black': type_of(m))
    Blackpencolb.grid(row=0, column=5, padx=10, pady=1)

    Createnewpencolb = Button(optionsframe, text='Createnewpencolimg', style='COLBG.TButton', command=choose_pen_color)
    Createnewpencolb.grid(row=1, column=5, padx=10, pady=1)

    widthlabel = Label(optionsframe, text='Width: ', style='LABELBG.TLabel')
    width = Scale(optionsframe, from_=1, to=20, style='SCALEBG.Horizontal.TScale')
    widthlabel.grid(row=0, column=6)
    width.grid(row=0, column=7)
    width.set(20)

    opacitylabel = Label(optionsframe, text='Opacity: ', style='LABELBG.TLabel')
    opacity = Scale(optionsframe, from_=0, to=1.0, style='SCALEBG.Horizontal.TScale')
    opacitylabel.grid(row=1, column=6)
    opacity.grid(row=1, column=7)
    opacity.set(1.0)


def setup(filelocation):
    global stage, img_id, optionsframe, draw

    for widgets in root.winfo_children():
        widgets.destroy()

    root.config(bg='#454545')
    iconsframewidth = int(screen_width / 20)

    frames = Style()
    frames.configure('FRAMES.TFrame', background='#2a2a2a')
    sep = Style()
    sep.configure('SEP.TFrame', background='#1a1a1a')
    style = Style()
    style.configure('STAGE.TFrame', background='#454545')
    icon = Style()
    icon.configure('ICON.TButton', background='#2a2a2a', foreground='#2a2a2a')

    iconsframe = Frame(root, width=iconsframewidth, style='FRAMES.TFrame')
    iconsframe.pack(side='left', expand=False, fill='y')
    iconsframe.pack_propagate(0)
    sep1frame = Frame(root, style='SEP.TFrame', width=5)
    sep1frame.pack(side='left', expand=False, fill='y')
    optionsframe = Frame(root, style='FRAMES.TFrame', height=100)
    optionsframe.pack(side='top', expand=False, fill='x')
    optionsframe.pack_propagate(0)
    sep2frame = Frame(root, style='SEP.TFrame', height=5)
    sep2frame.pack(side='top', expand=False, fill='x')
    propertyframe = Frame(root, style='FRAMES.TFrame', width=150)
    propertyframe.pack(side='right', expand=False, fill='y')
    propertyframe.pack_propagate(0)
    sep3frame = Frame(root, style='SEP.TFrame', width=5)
    sep3frame.pack(side='right', expand=False, fill='y')
    stageframe = Frame(root, style='STAGE.TFrame')
    stageframe.pack(side='top', expand=True, fill='both')
    stageframe.pack_propagate(0)

    image = Image.open(filelocation)
    width, height = image.size

    stage = Canvas(stageframe, width=width, height=height)
    stage.pack(side="top", anchor='c', expand=True)

    root.update()

    keyboard.add_hotkey("ctrl+s", lambda widget=stage, filelocation=filelocation: save(widget, filelocation))

    pencilbutton = Button(iconsframe, text='pencilimg', command=pencil_click, style='ICON.TButton')
    pencilbutton.pack(anchor=N, pady=10)

    imgtk = ImageTk.PhotoImage(Image.open(filelocation))
    img_id = stage.create_image(stage.winfo_width() / 2, stage.winfo_height() / 2, image=imgtk)
    stage.image = imgtk


root = tk.Tk()
root.title('App')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

w = 1150
h = 600
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.minsize(1150, 600)

setup('Test.png')
root.mainloop()
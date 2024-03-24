from tkinter import *

canvas_w = 700
canvas_h = 500
brush_size = 3
color = 'black'

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1,y1,x2,y2,
                  fill=color, outline=color)


def brush_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color





root = Tk()
root.title('Simple Paint')
root.geometry('700x400')
root.resizable(False, False)

w = Canvas(root, 
           width = canvas_w,
           height = canvas_w,
           bg= 'white')

w.bind('<B1-Motion>', paint)

#buttons

red_btn = Button(text="Red", width=10, command=lambda: color_change('red'))
black_btn = Button(text="Black", width=10, command=lambda: color_change('black'))
gre_btn = Button(text="Green", width=10, command=lambda: color_change('green'))
blu_btn = Button(text="Blue", width=10, command=lambda: color_change('blue'))
ora_btn = Button(text="Orange", width=10, command=lambda: color_change('orange'))
er_btn = Button(text="Eraser", width=10, command=lambda: color_change('white'))

btn5 = Button(text='Size: 5', width=10, command=lambda: brush_size_change(5))
btn8 = Button(text='Size: 8', width=10, command=lambda: brush_size_change(8))
btn3 = Button(text='Size: 3', width=10, command=lambda: brush_size_change(3))
btn15 = Button(text='Size: 15', width=10, command=lambda: brush_size_change(15))



w.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=W+E+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)




red_btn.grid(row=0, column=1)
black_btn.grid(row=0, column=2)
gre_btn.grid(row=0, column=3)
blu_btn.grid(row=0, column=4)
ora_btn.grid(row=0, column=5)
er_btn.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn5.grid(row=1, column=3)
btn8.grid(row=1, column=4)
btn15.grid(row=1, column=5)

root.mainloop()
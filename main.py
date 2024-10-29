from tkinter import *
import random

root = Tk()
root.geometry("800x600")
root.config(bg="purple")

''' MODEL '''
def change_radius(e):
    canvas.coords(circle, x_coor.get()-radius.get(), y_coor.get()-radius.get(), x_coor.get()+radius.get(), y_coor.get()+radius.get())

def move_square(delta_x,delta_y):
    left,top,right,bottom = canvas.coords(square)
    if left<10 or right > 770:
        delta_x *= -1
    if top<10 or bottom>480:
        delta_y *= -1
    canvas.move(square,delta_x,delta_y)
    canvas.after(20, lambda: move_square(delta_x, delta_y ))

def move_circle(event):
    key = event.keysym
    if key == "Left":
        x_coor.set(x_coor.get()-10)
        canvas.move(circle,-10, 0)
    elif key == "Right":
        x_coor.set(x_coor.get()+10)
        canvas.move(circle,10, 0)
    elif key == "Up":
        y_coor.set(y_coor.get()-10)
        canvas.move(circle,0, -10)
    else:
        y_coor.set(y_coor.get()+10)
        canvas.move(circle,0, 10)
    
x_coor = IntVar()
x_coor.set(390)

y_coor = IntVar()
y_coor.set(245)

radius = IntVar()
radius.set(10)

delta_x = random.randint(-5,-5)
delta_y = random.randint(-5,-5)

root.bind("<Left>", move_circle)
root.bind("<Right>", move_circle)
root.bind("<Up>", move_circle)
root.bind("<Down>", move_circle)

''' CONTROLLER '''
horizontal = Scale(root, from_ = 0, to = 250, orient = "horizontal", variable = radius, command = change_radius)
horizontal.place(x = 10, y = 20, width = 200)

''' VIEW '''
canvas = Canvas(root,bg = "orange")
canvas.place(x = 10, y = 100, width = 780, height =490)

square = canvas.create_rectangle(10,10,30,30,fill="red")

circle = canvas.create_oval(x_coor.get() - radius.get(), y_coor.get()-radius.get(), x_coor.get() + radius.get(), y_coor.get()+radius.get(), fill = "black" )

move_square(delta_x, delta_y)

root.mainloop()
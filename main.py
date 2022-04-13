from tkinter import Button
from Mibo.Mibo import Mibo

t = Mibo()
t.penup()
t.goto(0,-5)
t.pendown()
t.recatngle(5,5)
t.recatngleAreaAnimation(5,5)
#t.circle(2)


def press():
    t.recatngle(10,10)
canvas = t.screen.getcanvas()
btn = Button(canvas.master, text="This button exists in turtle",command=press)
btn.pack()
t.screen.mainloop()
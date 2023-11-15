""" OPTION A """
from turtle import *

shape("turtle")
speed(1)

def fractal_tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size * 2)
        color("black")
        return

    forward(size)
    right(angle)

    fractal_tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    fractal_tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)

left(90)

fractal_tree(70, 10, 45)



mainloop()
'''one blue mf eating red apples'''
import collections
import random
import turtle
from tkinter import *

w, h = [1000, 1000]
canvas = Canvas(width=w, height=h)
canvas.pack()

k = turtle.RawTurtle(turtle.TurtleScreen(canvas))
k.shape('square')
k.shapesize(3, 3, 2)
k.color("blue")
k.speed(6)
k.pu()

kruhs = collections.defaultdict(int)


def food_gen(n, size):
    for kruh_idx in range(n):
        x, y = random.randint(-w // 2, w // 2), random.randint(-h // 2, h // 2)
        oval = canvas.create_oval(x, y, x + size, y + size, fill='red', width=2)
        kruhs[kruh_idx] = oval


def movement(speed):
    k.fd(speed)

    for kruh_idx, oval in kruhs.items():
        overlapping = canvas.find_overlapping(*canvas.coords(oval))
        if k.turtle._item in overlapping:
            del kruhs[kruh_idx]
            canvas.delete(oval)
            break


canvas.focus_set()
canvas.bind('<w>', lambda event: k.setheading(90))
canvas.bind('<s>', lambda event: k.setheading(270))
canvas.bind('<a>', lambda event: k.setheading(180))
canvas.bind('<d>', lambda event: k.setheading(0))


def main(apples, size):
    food_gen(apples, size)
    while True:
        movement(3)
        canvas.update()

        if not kruhs:
            canvas.create_text(0, 0, text="YOU WON", fill='red', font=("Arial", 49), justify=CENTER)
            canvas.update()
            canvas.after(2000, canvas.master.quit())
            print("Game Over")
            return


if __name__ == "__main__":
    main(9, 50)

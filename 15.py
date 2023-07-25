import copy
import random
import tkinter as tk

root = tk.Tk()
print(f"Enter a number that determines the size of the grid: ", end='')
n = 4
size = 50
score = 0
c = tk.Canvas(root, width=n*size, height=n*size)
c.pack()


def draw():
    for i in range(n):
        for j in range(n):
            c.create_rectangle(j*size, i*size, j*size+size, i*size+size, fill='gray')

            txt = current_state[i][j]
            if current_state[i][j] == 16:
                txt = ' '
            c.create_text(j*size+size//2, i*size+size//2, text=str(txt))


def matrix_gen(arr):
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = arr[i*n+j]

    return matrix


nums = [i for i in range(1, n**2+1)]
valid_state = matrix_gen(nums)
random.shuffle(nums)
current_state = matrix_gen(nums)

#current_state = copy.deepcopy(valid_state)
#current_state[-2][-1], current_state[-1][-1] = current_state[-1][-1], current_state[-2][-1]  # Swap elements

draw()


def move(event):
    y, x = event.x // size, event.y // size  # Swap x and y

    global score

    change = None
    for i, j in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
        if 0 <= i < n and 0 <= j < n:
            if current_state[i][j] == 16:
                change = (i, j)
                break

    if change:
        i, j = change
        score += 1
        current_state[i][j], current_state[x][y] = current_state[x][y], current_state[i][j]
        draw()

    if valid_state == current_state:
        c.after(100)
        c.delete('all')
        c.create_text(n * size // 2, n * size // 2, text='score ' + str(score),
                      font=("Arial", n + 5), justify='center')
        c.update()


c.bind("<Button-1>", move)
c.mainloop()

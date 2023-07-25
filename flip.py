import random
import tkinter as tk
root = tk.Tk()
print(f"enter number that determines the size of the grid: ", end='')
#n = int(input().strip())
n=5
size = 100 ; score = 0 ; matrix = []
for i in range(n):
    tmp = [random.randint(0,1) for _ in range(n)]
    matrix.append(tmp)

c = tk.Canvas(root, width=n*size, height=n*size)
c.pack()

def booting_device_with_no_booty_whatsoever():
    colors = {0:'gray', 1:'white'}
    c.delete('all')

    for i in range(n):
        for j in range(n):
            c.create_rectangle(i*size,j*size, i*size+size, j*size+size, fill=colors[matrix[i][j]])

    c.update()

def the_end():
    if matrix == [[1 for i in range(n)] for j in range(n)] or matrix == [[0 for i in range(n)] for j in range(n)]:
        return True
    return False

def flip(event):
    global score
    x, y = event.x // size, event.y // size

    for i,j in [[x,y],[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
        if 0<=i<n and 0<=j<n:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            else: matrix[i][j] = 1

    score += 1
    booting_device_with_no_booty_whatsoever()
    c.after(100)
    c.update()

    if the_end():
        c.after(100)
        c.delete('all')
        c.create_text(n * size // 2, n * size // 2, text='score ' + str(score),
                      font=("Arial", n + 5), justify='center')
        c.update()



booting_device_with_no_booty_whatsoever()
c.bind("<Button-1>", flip)
c.mainloop()

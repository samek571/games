'''clear the board by clicking on a tile, the segment with the same color gets popped and the rest obeys gravity'''


import random
import tkinter as tk
root = tk.Tk()
print(f"enter number that determines the size of the grid: ", end='')
n = int(input().strip())
size = 50 ; clicks = 0
matrix = [[0 for j in range(n)] for i in range(n)] ; score=0
c = tk.Canvas(root, width=n*size, height=n*size)
c.pack()

def booting_device_with_no_booty_whatsoever():
    colors = {0:'blue', 1:'red', 2:'yellow', 3:'green'}

    for i in range(n):
        for j in range(n):
            num = random.randint(0,len(colors)-1)
            matrix[i][j] = colors[num]
            c.create_rectangle(i*size,j*size, i*size+size, j*size+size, fill=colors[num])


#drawing the board again
def draw():
    c.delete('all')
    for i in range(n):
        for j in range(n):
            colors = matrix[i][j]
            c.create_rectangle(i*size,j*size, i*size+size, j*size+size, fill=colors)
    c.update()


#arguably the best way to delete the gray shits
#just shifting so there is something like gravity
def gravity_falls():
    for i, row in enumerate(matrix):
        tmp = [] ; cnt = 0
        for value in row:
            if value != "gray":
                tmp.append(value)
            else:
                cnt += 1
        matrix[i] = ['gray'] * cnt + tmp

    draw()

def the_end():
    if matrix == [['gray' for j in range(n)] for i in range(n)]: return True
    return False

#iterative dfs_region - could be bfs if there would be pop(0)
#iterative is easier to debug and its just simulated recursion in the end
def dfs_region(event):
    global clicks
    x,y = event.x//size, event.y//size

    desired_color = matrix[x][y] ; q=[[x,y]] ; flag=True
    if desired_color == 'gray':
        flag = not flag
        clicks-=1

    while q and flag:
        row, col = q.pop()
        matrix[row][col] = 'gray'
        c.create_rectangle(row*size, col*size, row*size+size, col*size+size, fill='gray')

        for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:

            if 0<=row+i<n and 0<=col+j<n and matrix[row+i][col+j] == desired_color:
                q.append([row+i, col+j])

    clicks+=1
    c.update()
    c.after(100)
    gravity_falls()
    c.update()

    if the_end():
        c.after(100)
        c.delete('all')
        c.create_text(n*size//2,n*size//2, text='It took you ' + str(clicks) + ' clicks to beat the game', font=("Arial", n+5), justify='center')
        c.update()



booting_device_with_no_booty_whatsoever()
c.bind("<Button-1>", dfs_region)
c.mainloop()
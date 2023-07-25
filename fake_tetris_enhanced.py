'''clear the board by clicking on a tile, the segment with the same color gets popped and the rest obeys gravity
extra:

- if one column is full gray, rest shifts to the right
- option to lose the game by not playing smart - at least 2 colored segments has to be popped at one click
- (+tells you if it isnt possible to win anymore)
'''

"""
it ofc has to be handled differently - checking if its solveable, enhance the color generation to not be completly random...
"""


import copy
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
    global matrix
    grayed = set()
    for i, row in enumerate(matrix):
        tmp = [] ; cnt = 0
        for value in row:
            if value != "gray":
                tmp.append(value)
            else:
                cnt += 1
        matrix[i] = ['gray'] * cnt + tmp
        if cnt == n: grayed.add(i)

    #move gray columns at the end
    new=[]
    for i in range(n):
        if i not in grayed:
            new.append(matrix[i])

    for i in range(len(grayed)):
        new.append(['gray']*n)

    matrix = copy.deepcopy(new)

    draw()

def winning_verify():
    if matrix == [['gray' for j in range(n)] for i in range(n)]: return True
    return False

def losing_verify():
    for i in range(n):
        for j in range(n):

            if matrix[i][j] != 'gray':
                for x,y in [[i,j+1],[i,j-1],[i-1,j],[i+1,j]]:
                    if 0<=x<n and 0<=y<n and matrix[i][j] == matrix[x][y]: return True

    return False


#iterative dfs_region - could be bfs if there would be pop(0)
#iterative is easier to debug and its just simulated recursion in the end
def dfs_region(event):
    global clicks
    x,y = event.x//size, event.y//size
    desired_color = matrix[x][y] ; q=[[x,y]]


    #clicked on gray by accident = no harm
    def at_least_two_and_nongray():
        global clicks
        if desired_color != 'gray':
            for i, j in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= i < n and 0 <= j < n:
                    if matrix[i][j] == desired_color: return True

        clicks-=1
        print('fucking error')
        return False

    if at_least_two_and_nongray():
        while q:
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

        if winning_verify():
            c.after(100)
            c.delete('all')
            c.create_text(n*size//2,n*size//2, text='It took you ' + str(clicks) + ' clicks to beat the game', font=("Arial", n+5), justify='center')
            c.update()

        if not losing_verify():
            c.after(100)
            #c.delete('all')
            c.create_text(n*size//2,n*size//2, text='bozo ' + str(clicks), font=("Arial", n+5), justify='center')
            c.update()



booting_device_with_no_booty_whatsoever()
c.bind("<Button-1>", dfs_region)
c.mainloop()
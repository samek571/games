import collections
import copy
import random
import tkinter as tk
root = tk.Tk()
print(f"enter number that determines the size of the grid: ", end='')
#n = int(input().strip())
n=12
size = 50
matrix = [['' for j in range(n)] for i in range(n)] ; score=0
c = tk.Canvas(root, width=n*size, height=n*size)
c.pack()

colors = {0:'blue', 1:'red', 2:'yellow', 3:'green', 4:'purple', 5:'orange'}
def draw(booting_flag):

    c.delete('all')
    for i in range(n):
        for j in range(n):
            fillcolor = matrix[i][j]

            if booting_flag:
                num = random.randint(0,len(colors)-1)
                matrix[i][j] = colors[num]
                fillcolor = colors[num]

            c.create_rectangle(i*size,j*size, i*size+size, j*size+size, fill=fillcolor)

    c.update()


covered = set()
def bfs_expanding(event):
    global clicks, score
    x, y = event.x // size, event.y // size
    prev_color = matrix[0][0]; desired_color = matrix[x][y]

    flooded = set()
    q=collections.deque([[0,0]])
    score+=1
    while q:
        i,j = q.popleft()
        if 0<=i<n and 0<=j<n and (i,j) not in flooded and matrix[i][j] == prev_color:
            flooded.add((i,j))
            matrix[i][j]=desired_color
            for a,b in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
                q.append([a,b])


    draw(False)


    diversity = set() ; flag = True
    for i in range(n):
        for j in range(n):
            diversity.add(matrix[i][j])
            if len(diversity)>1:
                flag = False
                break

    if flag:
        c.after(500)
        c.delete('all')
        c.create_text(n * size // 2, n * size // 2, text='It took you ' + str(score) + ' moves to finish', font=("Arial", n + 5), justify='center')
        c.update()


draw(True)
c.bind("<Button-1>", bfs_expanding)
c.mainloop()
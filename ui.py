import tkinter as tk
import time
from random import shuffle

def createPuzzle(m, n):
    puzzle = [i for i in range(1, m*n+1)]
    return puzzle

def coloringPuzzle(list_button, puzzle, puzzle_size):
    for i in range(puzzle_size):
        if(puzzle[i] > 0):
            list_button[i].config(background = "green")
        else:
            list_button[i].config(background = "red")
        list_button[i].update

def setButtonPosition(m, n, root):
    list_button = []
    for i in range(m):
        for j in range(n):
            text_button = str(i*n+j+1)
            btn = tk.Button(root, text = text_button, width = 4, height = 3)
            btn.place(x = j*4, y = i*3)
            list_button.append(btn)
    return list_button


def ui(m, n):
    root = tk.Tk()  #init window
    root.title('A* Coloring Puzzle')
    window_size = "" + str(n*100) + "x" + str(m*100) + "+" + "200+200"
    root.geometry(window_size)    #size of window
    list_button = setButtonPosition(m, n, root)
    root.update()
    colors = ["red", "green"]

    puzzle = createPuzzle(m, n)

    while True:
        for i in range(0,len(colors)):
            btn1.config(background=colors[i])
            btn1.update()
            time.sleep(1)
        root.mainloop()

ui(3, 4)
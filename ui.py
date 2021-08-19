from tkinter import * 
import time
from random import shuffle

def coloringPuzzle(list_label, green_list, red_list, time_sleep):
    for i in range(len(green_list)):
        if(list_label[green_list[i]-1].cget("bg") == "red"):
            list_label[green_list[i]-1].config(bg = "green")
            list_label[green_list[i]-1].update()
            time.sleep(time_sleep)
    for i in range(len(red_list)):
        if(list_label[red_list[i]-1].cget("bg") == "green"):
            list_label[red_list[i]-1].config(bg= "red")
            list_label[red_list[i]-1].update()
            time.sleep(time_sleep)



def setLabelPosition(m, n, root):
    list_label = []
    for i in range(m):
        for j in range(n):
            text_label = str(i*n+j+1)
            btn = Label(root, text = text_label, width = 6, height = 3, bg = "green", relief="groove", borderwidth=1)
            btn.grid(row=i+5, column =j)
            list_label.append(btn)
    return list_label

'''
def ui(m, n):
    root = tk.Tk()
    root.geometry("400x200+200+200")
    btn1 = tk.label(root, text="butn_3")
    btn1.place(relx=0.2, rely=0.5)
    root.update()
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "cyan"]
    while True:
        shuffle(colors)
        for i in range(0,len(colors)):
            btn1.config(background=colors[i])
            btn1.update()
            time.sleep(1)
    root.mainloop()
'''

def createUI(m, n):
    window = Tk()
    window_size = "" + str(m*60) + "x" + str(n*60+50) + "+" + "200+200"
    window.geometry(window_size)
    window.title("A* GUI")
    
    list_label = setLabelPosition(m, n, window)
    return window, list_label

def updateUI(m, n, window, list_label, red_list, green_list, time_sleep):
    lis_label = coloringPuzzle(list_label, green_list, red_list, time_sleep)
    window.update()

m = 5
n = 5
red_list = [1, 2, 3, 6, 7, 9]
green_list = [4, 5, 8, 9]
window, list_label = createUI(m, n)
updateUI(m, n, window, list_label, red_list, green_list, 0.5)
window.mainloop()
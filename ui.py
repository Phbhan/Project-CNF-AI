from tkinter import * 
import time
from random import shuffle
from tkinter import filedialog

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
'''
def coloringPuzzle(list_label, green_lable, red_lable, time_sleep):
    if(list_label[green_lable-1].cget("bg") == "red"):
        list_label[green_lable-1].config(bg = "green")
        list_label[green_lable-1].update()
        time.sleep(time_sleep)
    if(list_label[red_lable-1].cget("bg") == "green"):
        list_label[red_lable-1].config(bg = "red")
        list_label[red_lable-1].update()
        time.sleep(time_sleep)
'''

def setLabelPosition(m, n, window):
    list_label = []
    for i in range(m):
        for j in range(n):
            text_label = str(i*n+j+1)
            lb = Label(window, text = text_label, width = 6, height = 3, bg = "green", relief="groove", borderwidth=1)
            lb.grid(row=i, column =j+6)

            list_label.append(lb)
    return list_label

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*"))) 

    return filename
    # Change label contents


def createUI(m, n):
    window = Tk()
    window_size = "" + str(n*60+210) + "x" + str(m*60-20) + "+" + "200+200"
    window.geometry(window_size)
    window.title("A* GUI")

    label_file_explorer = Label(window,
                    text = "Open a File",
                    width = 30, height = 1,
                    fg = "blue", anchor="n")
    label_file_explorer.grid(column = 0, row = 0)   
    browse_button = Button(window,
                        text = "Browse",
                        command = browseFiles, anchor = 's') 
    browse_button.grid(row = 1, column = 0)
    filename = browse_button.cget("command")
    label_file_explorer.configure(text=filename)

    label_heuristic = Label(window,
                    text = "Heuristic",
                    width = 10, height = 1,
                    fg = "black", anchor="sw")
    label_heuristic.place(x=2, y = 110) 

    label_heuristic_value = Label(window,
                    text = "149",
                    width = 10, height = 1,
                    fg = "red", anchor="sw")
    label_heuristic_value.place(x=65, y = 110) 

    label_speed = Label(window,
                    text = "Speed",
                    width = 5, height = 1,
                    fg = "black", anchor="sw") 
    label_speed.place(x=2, y=155)

    entry = Entry(window, width = 15) 
    entry.place(x=60, y=155)
    
    start_button = Button(window, text = "Start")
    start_button.place(x=100, y =  195)

    update_button = Button(window, text = "Update")
    update_button.place(x=2, y = 195)
    
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

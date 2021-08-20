from GenerateCNF import generateCNF
from file import *
from pysat.solvers import Glucose3
import numpy as np
from Astart import Astart
from ui import *
import time


def get_variable(vars, cells):
    for i in cells:
        if i not in vars:
            vars.append(i)


def showMessageBox():
    messagebox.showwarning("Error","No Solution")  

def runAStar(vars, clauses, isSolvable):
    data = readFile()
    m = data[0]
    n = data[1]
    matrix_inp = data[2]

    print(matrix_inp)
    window, list_label = createUI(m, n, matrix_inp)

    label_heuristic_value = Label(window,

                    text = "",
                    width = 10, height = 1,
                    fg = "red", anchor="sw")
    label_heuristic_value.place(x=75, y = 110)

    label_step_value = Label(window,
                    text = "0",
                    width = 10, height = 1,
                    fg = "red", anchor="sw")
    label_step_value.place(x=75, y = 155)  


    entry = Entry(window, width=15)
    entry.place(x=60, y=200)

    update_button = Button(window, text="Update")
    update_button.place(x=5, y=230)
    if(isSolvable == True):
        start_button = Button(window, text = "Start", command = lambda:Astart(clauses, vars, window, list_label, label_heuristic_value, 0.5, label_step_value))
        start_button.place(x=100, y =  230)

    else:
        start_button = Button(window, text="Start", command=showMessageBox)
        start_button.place(x=100, y=230)

    # Run A*
    window.mainloop()


def main():

    data = []
    vars = []
    data = readFile()
    m = data[0]
    n = data[1]
    inp = data[2]
    #print("Input infor:", m, n, inp)

    clause = []
    for i in range(0, m):
        for j in range(0, n):
            if(inp[i][j] != -1):
                cells = []
                clause = generateCNF(m, n, i, j, inp[i][j], cells, clause)
                if (clause == False):
                    break
                get_variable(vars, cells)



    '''
    start = time.time()
    print(Astart(clause, vars))
    end = time.time()
    print("Measure time: ", end-start)
    '''
    g = Glucose3()
    for it in clause:
        g.add_clause([int(k) for k in it])
    if(g.solve()):
        model = g.get_model()
        print(model)

        for i in range(m):
            for j in range(n):
                if (i*n+j+1 > 0) and (i*n+j+1 in model):
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print('')

    runAStar(vars, clause, g.solve())



main()

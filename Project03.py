from GenerateCNF import generateCNF
from file import *
from pysat.solvers import Glucose3
import numpy as np
from Astart import Astart
import time


def get_variable(vars, cells):
    for i in cells:
        if i not in vars:
            vars.append(i)


def main():

    data = []
    vars = []
    data = readFile()
    m = data[0]
    n = data[1]
    inp = data[2]
    print("Input infor:", m, n, inp)

    clause = []
    for i in range(0, m):
        for j in range(0, n):
            if(inp[i][j] != -1):
                cells = []
                clause = generateCNF(m, n, i, j, inp[i][j], cells, clause)
                get_variable(vars, cells)

    start = time.time()
    print(Astart(clause, vars))
    end = time.time()
    print("Measure time: ", end-start)

    g = Glucose3()
    for it in clause:
        g.add_clause([int(k) for k in it])
    print(g.solve())
    model = g.get_model()
    print(model)

    for i in range(m):
        for j in range(n):
            if (i*n+j+1 > 0) and (i*n+j+1 in model):
                print('1', end=' ')
            else:
                print('0', end=' ')
        print('')


main()

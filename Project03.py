from GenerateCNF import generateCNF
from file import *
from pysat.solvers import Glucose3
import numpy as np

def main():
    # m = 2
    # n = 2
    # inp = [[1, -1], [-1, 1]]
    # m = 3
    # n = 3
    # inp = [[-1, -1, -1], [-1, 2, -1], [-1, -1, -1]]

    tmp = []
    tmp = readFile()
    m = tmp[0]
    n = tmp[1]
    inp = tmp[2]
    print("Input infor:", m, n, inp)

    clause = []
    for i in range(0, m):
        for j in range(0, n):
            if(inp[i][j] != -1):
                generateCNF(m, n, i, j, inp[i][j], clause)
    g = Glucose3()
    for it in clause:
        g.add_clause([int(k) for k in it])
    print(g.solve())
    model = g.get_model()
    print(model)

    for i in range(m):
        for j in range(n):
            if model[i+j] > 0:
                print('1', end=' ')
            else: print('0', end=' ')
        print('')

main()

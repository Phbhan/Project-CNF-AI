from GenerateCNF import generateCNF
from file import *
from pysat.solvers import Glucose3
import numpy as np
from Astart import Astart

def get_variable(vars, cells):
    for i in cells:
        if i not in vars:
            vars.append(i)

def readTestFile(file_index):
    n = 0
    m = 0
    inp = []
    filename = f"input{file_index}.txt"
    if not os.path.isfile(filename):
        print('File does not exist.')
    else:
        file = open(filename, 'r')

        line = file.readline()
        tmp = line.split()
        m = int(tmp[0])
        n = int(tmp[1])

        for i in range(m):
            line = file.readline()
            tmp = line.split()
            tmp_inp = []
            for j in range(n):
                if(tmp[j] != "."):
                    tmp_inp.append(int(tmp[j]))
                else:
                    tmp_inp.append(-1)
            inp.append(tmp_inp)

        file.close()
    
    filename = f"output{file_index}.txt"
    if not os.path.isfile(filename):
        print('File does not exist.')
    else:
        file = open(filename, 'r')
    out = []
    for i in range(m):
        out.append(map(int, file.readline().split()))

    return m, n, inp, out



def checkResult(real_result, model_result):
    m, n = len(real_result), len(real_result[0])
    for i in range(m):
        for j in range(n):
            if real_result[i][j] != model_result[i][j]:
                return False
    return True

def main():
    print("How many test?", end = " ")
    n_test = int(input())
    for t in range(n_test):
        m, n, inp, out = readTestFile(t)
        print("Input infor:", m, n, inp)
        temp = readTestFile("")
        inp = temp[2]
        clause = []
        for i in range(0, m):
            for j in range(0, n):
                if(inp[i][j] != -1):
                    cells = []
                    clause = generateCNF(m, n, i, j, inp[i][j], cells, clause)
                    get_variable(vars, cells)
        # print(vars)
        #clause = [[1, 2], [1, -2]]
        print(clause)
        print(Astart(clause, vars))
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
        result = [ [-1]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (i*n+j+1 > 0) and (i*n+j+1 in model):
                    result[i][j] = 1
                else:
                    result[i][j] = 0

        print(checkResult(out, result))


main()

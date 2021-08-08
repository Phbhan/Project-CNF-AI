from GenerateCNF import generateCNF
from file import *


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


main()

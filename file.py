import os.path


def readFile():
    n = 0
    m = 0
    inp = []
    filename = "input.txt"
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
    return [m, n, inp]

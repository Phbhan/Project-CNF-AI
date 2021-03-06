import random

def generateOutputMatrix(m, n):
    output_matrix = [[random.randint(0,1) for j in range(n)] for i in range(m)]
    return output_matrix

def generateInputMatrix(output_matrix):
    delta = [ (0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
    def isValid(m, n, cur_pos):
        return 0 <= cur_pos[0] < m and 0 <= cur_pos[1] < n
    
    m, n = len(output_matrix), len(output_matrix[0])
    input_matrix = [ [-1] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            # đếm số ô xanh xung quanh ô (i, j)
            count = 0
            for k in range(len(delta)):
                next_x, next_y = i + delta[k][0], j + delta[k][1]
                if isValid(m, n, (next_x, next_y)):
                    if output_matrix[next_x][next_y] == 1:
                        count += 1
            if count == 0:
                count = '.'
            input_matrix[i][j] = count
    return input_matrix
    
def writeInput(file_name, matrix):
    m, n = len(matrix), len(matrix[0])
    f = open(file_name, 'w')
    f.write(f'{m} {n}\n')
    for i in range(len(matrix)):
        f.write(" ".join(map(str, matrix[i])) + '\n')
    f.close()

def writeOuput(file_name, matrix):
    f = open(file_name, 'w')
    for i in range(len(matrix)):
        f.write(" ".join(map(str, matrix[i])) + '\n')
    f.close()

def generateATest(m = 10, n = 10):
    output_matrix = generateOutputMatrix(m, n)
    input_matrix = generateInputMatrix(output_matrix)
    return input_matrix, output_matrix

if __name__ == "__main__":
    print("What value of m n you want?", end = " ")
    m, n = map(int, input().split())

    input, output = generateATest(m, n)

    input_file_name = f'input1.txt'
    writeInput(input_file_name, input)
    output_file_name = f'output1.txt'
    writeOuput(output_file_name, output)
        

        

from file import *
from copy import deepcopy

delta = [ (0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]

def isValid(m, n, cur_pos):
    return 0 <= cur_pos[0] < m and 0 <= cur_pos[1] < n

def satisfied(matrix, result_matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] < 0:
                continue
            # đếm số ô xanh xung quanh ô (i, j)
            count = 0
            all_assigned = True
            for k in range(len(delta)):
                next_x, next_y = i + delta[k][0], j + delta[k][1]
                if isValid(m, n, (next_x, next_y)):
                    # Tồn tại ô kề của ô (i, j) chưa được gán giá trị --> Không xét ô (i, j)
                    if result_matrix[next_x][next_y] == -1:
                        all_assigned = False
                        break
                    if result_matrix[next_x][next_y] == 1:
                        count += 1
            # nếu tất cả các ô xung quanh đã được gán mà số ô xanh không bằng --> False
            if all_assigned and count != matrix[i][j]:
                return False
    return True

def bruteforce(m, n, matrix, result_matrix, index):
    if index == m * n:
        if satisfied(matrix, result_matrix):
            return True, result_matrix
        return False, [[]]

    x, y = index // m, index % n
    # print(index, x, y, result_matrix)

    green = True
    # nếu có ô nào xung quanh là 0 thì không được đặt màu xanh tại ô cur_pos
    for i in range(len(delta)):
        next_x, next_y = x + delta[i][0], y + delta[i][1]
        if (isValid(m, n, (next_x, next_y)) and matrix[next_x][next_y] == 0):
            green = False
            break

    # thử đặt màu đỏ
    temp_result_matrix = deepcopy(result_matrix)
    temp_result_matrix[x][y] = 0
    found_solution, solution = bruteforce(m, n, matrix, temp_result_matrix, index + 1) 
    if found_solution:
        return found_solution, solution

    # thử đặt màu xanh nếu được
    if green:
        temp_result_matrix = deepcopy(result_matrix)
        temp_result_matrix[x][y] = 1
        found_solution, solution = bruteforce(m, n, matrix, temp_result_matrix, index + 1) 
        if found_solution:
            return found_solution, solution
    
    return False, [[]]


def backtrack(m, n, matrix, result_matrix, index):
    if satisfied(matrix, result_matrix):
        if index == m * n:
            return True, result_matrix
    else:
        return False, [[]]

    x, y = index // m, index % n
    # print(index, x, y, result_matrix)

    green = True
    # nếu có ô nào xung quanh là 0 thì không được đặt màu xanh tại ô cur_pos
    for i in range(len(delta)):
        next_x, next_y = x + delta[i][0], y + delta[i][1]
        if (isValid(m, n, (next_x, next_y)) and matrix[next_x][next_y] == 0):
            green = False
            break

    # thử đặt màu đỏ
    temp_result_matrix = deepcopy(result_matrix)
    temp_result_matrix[x][y] = 0
    found_solution, solution = backtrack(m, n, matrix, temp_result_matrix, index + 1) 
    if found_solution:
        return found_solution, solution

    # thử đặt màu xanh nếu được
    if green:
        temp_result_matrix = deepcopy(result_matrix)
        temp_result_matrix[x][y] = 1
        found_solution, solution = backtrack(m, n, matrix, temp_result_matrix, index + 1) 
        if found_solution:
            return found_solution, solution
    
    return False, [[]]



if __name__ == "__main__":
    m, n, matrix = readFile()
    solution = [[-1] * n for i in range(m)]
    # found, solution = bruteforce(m, n, matrix, solution, 0)
    # print("Brute force solution: ", solution)

    solution = [[-1] * n for i in range(m)]
    found, solution = backtrack(m, n, matrix, solution, 0)
    print("Backtrack solution: ", solution)
    # outputFile(solution)


from copy import deepcopy


def recursive(cells, sign, clause, tmp_clause, count_pos, count_neg, k):
    if(sign == "+"):
        if(len(tmp_clause) == count_pos):
            if not(tmp_clause in clause):
                clause.append(deepcopy(tmp_clause))
            return
    else:
        if(len(tmp_clause) == count_neg):
            if not(tmp_clause in clause):
                clause.append(deepcopy(tmp_clause))
            return
    if (k == len(cells)):
        return

    for i in range(k, len(cells)):
        if(sign == "+"):
            tmp_clause.append(cells[i])
        else:
            tmp_clause.append(-cells[i])
        recursive(cells, sign, clause, tmp_clause, count_pos, count_neg, i + 1)
        tmp_clause.pop(-1)
    return


def generateCNF(m, n, i, j, value, cells, clause):
    count = 1
    index = 0
    if (i-1) >= 0 and (j-1) >= 0:
        count += 1
        index = (i-1)*n + (j-1) + 1
        cells .append(index)
    if (i-1) >= 0:
        count += 1
        index = (i-1)*n + j+1
        cells .append(index)
    if (i-1) >= 0 and (j+1) < n:
        count += 1
        index = (i-1)*n + (j+1)+1
        cells .append(index)
    if (j-1) >= 0:
        count += 1
        index = i*n + (j-1)+1
        cells .append(index)

    index = i*n+j+1
    cells .append(index)

    if (j+1) < n:
        count += 1
        index = i*n + (j+1)+1
        cells .append(index)
    if (i+1) < m and (j-1) >= 0:
        count += 1
        index = (i+1)*n + (j-1)+1
        cells .append(index)
    if (i+1) < m:
        count += 1
        index = (i+1)*n + j+1
        cells .append(index)
    if (i+1) < m and (j+1) < n:
        count += 1
        index = (i+1)*n + (j+1)+1
        cells .append(index)

    count_pos = count - value + 1
    count_neg = value + 1
    #print("cells:", cells)

    recursive(cells, "+", clause, [], count_pos, count_neg, 0)
    recursive(cells, "-", clause, [], count_pos, count_neg, 0)
    #print("clause:", clause)
    return clause

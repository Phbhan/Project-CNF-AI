from copy import deepcopy


class priorQueue:
    def __init__(self):
        self.list = []

    def push(self, state):
        self.list.append(state)

    def pop(self):
        max_val_gx = -1000000
        max_val_fx = -1000000
        index = 0
        for i in range(len(self.list)-1, -1, -1):
            if max_val_gx < self.list[i]["gx"]:
                max_val_gx = self.list[i]["gx"]
                max_val_fx = self.list[i]["fx"]
                index = i
            elif max_val_gx == self.list[i]["gx"] and max_val_fx < self.list[i]["fx"]:
                max_val_fx = self.list[i]["fx"]
                index = i
        return self.list.pop(index)

    def get_len(self):
        return len(self.list)


def countClauseAfterAssigned(clauses, vars, state, var, val):
    #print(var, val, state)
    count_satisfiedClause = 0
    count_unsatisfiedClause = 0
    count_conflictClause = 0

    max_var = max(vars)
    check_var = [-1 for i in range(max_var + 1)]
    for i in state["1"]:
        check_var[i] = 1
    for i in state["0"]:
        check_var[i] = 0
    #print(state, var, val)
    # print(check_var)
    check_usf = []
    usf_clauses = []
    for clause in clauses:
        count = 0
        is_satisfied = False
        for x in clause:
            # print(x)
            if (x > 0 and check_var[x] == -1) or (x < 0 and check_var[-x] == -1):
                count += 1
            elif (x > 0 and check_var[x] == 1) or (x < 0 and check_var[-x] == 0):
                is_satisfied = True
                break
                # print(clause)

        if is_satisfied == True:
            count_satisfiedClause += 1
        else:
            if count == 0:
                return False
            usf_clauses.append(clause)
            count_unsatisfiedClause += 1

    #print(state, usf_clauses)
    is_satisfied_all = False
    # print(usf_clauses)
    while(not is_satisfied_all):
        is_satisfied_all = True
        i = 0
        while(i < len(usf_clauses)):
            # print(usf_clauses[i])
            tmp = []
            is_satisfied = False
            for x in usf_clauses[i]:
                if (x > 0 and check_var[x] == -1) or (x < 0 and check_var[-x] == -1):
                    tmp.append(x)
                elif (x > 0 and check_var[x] == 1) or (x < 0 and check_var[-x] == 0):
                    is_satisfied = True
                    break
            if is_satisfied == False:
                if len(tmp) == 0:
                    count_conflictClause += 1
                    # print(usf_clauses[i])
                    usf_clauses.remove(usf_clauses[i])
                    i = i-1
                elif len(tmp) == 1:
                    #print(tmp, check_var)
                    if tmp[0] > 0:
                        check_var[tmp[0]] = 1
                    else:
                        check_var[-tmp[0]] = 0
                    usf_clauses.remove(usf_clauses[i])
                    i = i-1
                    #print(tmp[0], u_clause, usf_clauses)
                    is_satisfied_all = False
            i += 1

    count_not_conflictClause = count_unsatisfiedClause - count_conflictClause
    return [count_satisfiedClause, count_not_conflictClause]


def get_unassigned_vars(vars, state):
    unassigned_vars = deepcopy(vars)
    for var in state["0"]:
        unassigned_vars.remove(var)
    for var in state["1"]:
        unassigned_vars.remove(var)
    return unassigned_vars


def Astart(clauses, vars):
    pq = priorQueue()
    var_max = max(vars)
    count_var = [0 for i in range(var_max+1)]
    for clause in clauses:
        for x in clause:
            if (x > 0):
                count_var[x] += 1
            else:
                count_var[-x] += 1
    count_max = 0
    var = 0
    for i in range(len(count_var)):
        if count_var[i] > count_max:
            count_max = count_var[i]
            var = i

    state0 = {}
    state0["1"] = []
    state0["0"] = [var]
    tmp = countClauseAfterAssigned(clauses, vars, state0, var, 0)
    #print(var, 0, tmp)
    if not (tmp == False):
        state0["gx"] = tmp[0]+tmp[1]
        state0["fx"] = tmp[0]
        pq.push(state0)
    state1 = {}
    state1["0"] = []
    state1["1"] = [var]
    tmp = countClauseAfterAssigned(clauses, vars, state1, var, 1)
    #print(var, 1, tmp)
    if not (tmp == False):
        state1["gx"] = tmp[0]+tmp[1]
        state1["fx"] = tmp[0]
        pq.push(state1)

    while(True):
        state = pq.pop()
        print(state)
        unasgn_vars = get_unassigned_vars(vars, state)
        # print(unasgn_vars)
        for var in unasgn_vars:
            #print('var:', var)

            new_state1 = deepcopy(state)
            new_state1["1"].append(var)
            tmp = countClauseAfterAssigned(clauses, vars, new_state1, var, 1)
            if not (tmp == False):
                new_state1["gx"] = tmp[0]+tmp[1]
                new_state1["fx"] = tmp[0]
                # print(new_state1["gx"])
                if tmp[0] == len(clauses):
                    return new_state1
                pq.push(new_state1)

            new_state0 = deepcopy(state)
            new_state0["0"].append(var)
            tmp = countClauseAfterAssigned(clauses, vars, new_state0, var, 0)
            if not (tmp == False):
                new_state0["gx"] = tmp[0]+tmp[1]
                new_state0["fx"] = tmp[0]
                # print(new_state0["gx"])
                check = 1
                if tmp[0] == len(clauses):
                    return new_state0
                pq.push(new_state0)
            break
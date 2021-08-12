from copy import deepcopy


class priorQueue:
    def __init__(self):
        self.list = []

    def push(self, state):
        self.list.append(state)

    def pop(self):
        max_val = 0
        index = 0
        for i in range(len(self.list)):
            if max_val < self.list[i]["gx"]:
                max_val = self.list[i]["gx"]
                index = i
        return self.list.pop(index)

    def get_len(self):
        return len(self.list)


def countClauseAfterAssigned(clauses, vars, state, var, val):
    count_satisfiedClause = 0
    count_unsatisfiedClause = 0
    max_var = max(vars)
    check_var = [-1 for i in range(max_var + 1)]
    for i in state["1"]:
        check_var[i] = 1
    for i in state["0"]:
        check_var[i] = 0
    #print(state, var, val)
    # print(check_var)
    for clause in clauses:
        count = 0
        is_satisfied = False
        is_var = False
        for x in clause:
            # print(x)
            if (x > 0 and check_var[x] == -1) or (x < 0 and check_var[-x] == -1):
                count += 1
            elif (x > 0 and check_var[x] == 1) or (x < 0 and check_var[-x] == 0):
                is_satisfied = True
                # print(clause)
            if x == var or x == -var:
                is_var = True
        if is_satisfied == True:
            count_satisfiedClause += 1
        else:
            if count == 0:
                return False
            if is_var == True:
                count_unsatisfiedClause += 1

    return [count_satisfiedClause, count_unsatisfiedClause]


def get_unassigned_vars(vars, state):
    unassigned_vars = deepcopy(vars)
    for var in state["0"]:
        unassigned_vars.remove(var)
    for var in state["1"]:
        unassigned_vars.remove(var)
    return unassigned_vars


def Astart(clauses, vars):
    pq = priorQueue()
    for var in vars:
        state1 = {}
        state1["0"] = []
        state1["1"] = [var]
        tmp = countClauseAfterAssigned(clauses, vars, state1, var, 1)
        #print(var, 1, tmp)
        if not (tmp == False):
            state1["gx"] = tmp[0]-tmp[1]
            pq.push(state1)
        state0 = {}
        state0["1"] = []
        state0["0"] = [var]
        tmp = countClauseAfterAssigned(clauses, vars, state0, var, 0)
        #print(var, 0, tmp)
        if not (tmp == False):
            state0["gx"] = tmp[0]-tmp[1]
            pq.push(state0)

    while(True):
        state = pq.pop()
        print(state)
        if state["gx"] == len(clauses):
            return state
        unasgn_vars = get_unassigned_vars(vars, state)
        # print(unasgn_vars)
        for var in unasgn_vars:
            new_state1 = deepcopy(state)
            new_state1["1"].append(var)
            tmp = countClauseAfterAssigned(clauses, vars, new_state1, var, 1)
            if not (tmp == False):
                new_state1["gx"] = tmp[0]-tmp[1]
                pq.push(new_state1)
            new_state0 = deepcopy(state)
            new_state0["0"].append(var)
            tmp = countClauseAfterAssigned(clauses, vars, new_state0, var, 0)
            if not (tmp == False):
                new_state0["gx"] = tmp[0]-tmp[1]
                pq.push(new_state0)


#print(Astart([[1, 2], [-1, -2], [2, 4], [3]], [1, 2, 3, 4]))

from copy import deepcopy
from ui import *

MIN = -1000000


class priorQueue_State:
    def __init__(self):
        self.list = []

    def push(self, state):
        self.list.append(state)

    def pop(self):
        max_val_gx = MIN
        max_val_fx = MIN
        index = 0
        for i in range(len(self.list)):
            if max_val_fx < self.list[i]["fx"]:
                max_val_fx = self.list[i]["fx"]
                max_val_gx = self.list[i]["gx"]
                index = i
            elif max_val_fx == self.list[i]["fx"] and max_val_gx < self.list[i]["gx"]:
                max_val_gx = self.list[i]["gx"]
                index = i

        return self.list.pop(index)

    def get_len(self):
        return len(self.list)


def countClauseAfterAssigned(clauses, vars, state):
    count_satisfiedClause = 0
    count_unsatisfiedClause = 0
    count_conflictClause = 0

    var_max = max(vars)
    check_var = [-1 for i in range(var_max + 1)]
    for i in state["1"]:
        check_var[i] = 1
    for i in state["0"]:
        check_var[i] = 0

    usf_clauses = []
    for clause in clauses:
        count = 0
        is_satisfied = False
        for var in clause:
            if (var > 0 and check_var[var] == -1) or (var < 0 and check_var[-var] == -1):
                count += 1
            elif (var > 0 and check_var[var] == 1) or (var < 0 and check_var[-var] == 0):
                is_satisfied = True
                break

        if is_satisfied == True:
            count_satisfiedClause += 1
        else:
            if count == 0:
                return False
            usf_clauses.append(clause)
            count_unsatisfiedClause += 1

    is_satisfied_all = False
    while(not is_satisfied_all):
        is_satisfied_all = True
        i = 0
        while(i < len(usf_clauses)):
            unassigned_var = []
            is_satisfied = False
            for var in usf_clauses[i]:
                if (var > 0 and check_var[var] == -1) or (var < 0 and check_var[-var] == -1):
                    unassigned_var.append(var)
                elif (var > 0 and check_var[var] == 1) or (var < 0 and check_var[-var] == 0):
                    is_satisfied = True
                    break

            if is_satisfied == False:
                if len(unassigned_var) == 0:
                    count_conflictClause += 1
                    usf_clauses.remove(usf_clauses[i])
                    continue
                elif len(unassigned_var) == 1:
                    var = unassigned_var[0]
                    if var > 0:
                        check_var[var] = 1
                    else:
                        check_var[-var] = 0
                    usf_clauses.remove(usf_clauses[i])
                    is_satisfied_all = False
                    continue
            i += 1

    count_not_conflictClause = count_unsatisfiedClause - count_conflictClause
    return [count_satisfiedClause, count_not_conflictClause]


def get_var(clauses, vars):
    count_var = {}
    for var in vars:
        count_var[var] = 0
    for clause in clauses:
        for var in clause:
            if (var > 0):
                count_var[var] += 1
            else:
                count_var[-var] += 1
    count_var = sorted(count_var.items(), key=lambda x: x[1], reverse=True)
    var = []
    for cv in count_var:
        var.append(cv[0])
    return var


def Astart(clauses, vars, window, list_label, label_heuristic_value, time_sleep, label_step_value):

    pq = priorQueue_State()
    return_state = False
    unassigned_vars = get_var(clauses, vars)

    state = {}
    state["index"] = 0
    state["0"] = []
    state["1"] = []
    state["fx"] = len(clauses)
    state["gx"] = 0
    pq.push(state)

    while(pq.get_len() > 0):
        state = pq.pop()
        if state["fx"] < len(clauses):
            break
        print(state)
        label_heuristic_value.config(text = str(state["fx"]-state["gx"]))
        label_heuristic_value.update()
        label_step_value.config(text = str(state["index"]))
        updateUI(window, list_label, state["0"], state["1"], time_sleep)
        var = unassigned_vars[state["index"]]

        new_state0 = deepcopy(state)
        new_state0["0"].append(var)
        gxhx = countClauseAfterAssigned(clauses, vars, new_state0)
        '''
        '''
        if not (gxhx == False):
            new_state0["fx"] = gxhx[0]+gxhx[1]
            new_state0["gx"] = gxhx[0]
            new_state0["index"] = state["index"] + 1
            check = 1
            if gxhx[0] == len(clauses):
                return_state = new_state0
                break
            pq.push(new_state0)

        new_state1 = deepcopy(state)
        new_state1["1"].append(var)
        gxhx = countClauseAfterAssigned(clauses, vars, new_state1)
        if not (gxhx == False):
            new_state1["fx"] = gxhx[0]+gxhx[1]
            new_state1["gx"] = gxhx[0]
            new_state1["index"] = state["index"] + 1
            if gxhx[0] == len(clauses):
                return_state = new_state1
                break
            pq.push(new_state1)
        '''
        print('1: ', new_state1["1"])
        print('0: ', new_state0["0"])
        '''

    return return_state


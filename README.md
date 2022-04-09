# Project-CNF-AI
## Group member and assigment:
Full Name | Assignment|
| :---:| :---: |
Phạm Bảo Hân | Generate CNF, Apply A* to solve CNF|
Long Mỹ Du | Program brute-force and backtracking|
Võ Nhất Huy | Use pysat library to solve CNF, Graphic interface|

## Problem statement:
You are asked to build a coloring puzzle solver by using the first order logic to CNF as
described below:

Given a matrix of size 𝑚 × 𝑛, where each cell will be a non-negative integer or zero
(empty cell). Each cell is considered to be adjacent to itself and 8 surrounding cells.

Your puzzle needs to color all the cells of the matrix with either blue or red, so that the
number inside each cell corresponds to the number of blue squares adjacent to that cell (see
Figure 1)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![Figure1](https://user-images.githubusercontent.com/62047983/162444937-9cbee1ab-1385-4530-b2a7-8332aa1ebb96.png)


In order to solve this problem, you can consider some steps:
* A logical variable is assigned to each cell of the matrix (If the logical variable of
that cell is True, it will be colored blue, otherwise it will be red)
* Write constraints for cells containing numbers to obtain a set of constraint clauses
in CNF (note that you need to remove duplicate clauses)
* Then, using the pysat library or the A* algorithm to find the value for each
variable and infer the result.
  * With A*, students asked to design the application with the interface as
shown that allows users to browse the input file as well as enter the delay
time for each step (default is 0.5s). See Figure 2.
  * When the user presses the Start button, runs the A* algorithm, at each step,
the state of the current State is displayed on the form, the step order and the
current State's heuristic value are also displayed on the form.
  * Students can use Python's tkinter library to create GUI

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![Figure2](https://user-images.githubusercontent.com/62047983/162444947-04150b07-2d85-46dd-84a4-f375fc9c2580.png)
  
## Overall plan for approaching the problem:
* Program brute-force and backtracking algorithm to have a deeper
understanding of the problem.
* Using CNF clauses and A*:
  * Find the appropriate CNF clause and the logical principle for generating
it. Programing the CNF generation.
  * Research pySAT. Programing it to solve the CNF clause. Test our CNF
generation program with pySAT.
  * Using A* to solve the CNF clause.
* Compare using A* solving CNF clause with brute-force and backtracking algorithm.
## Aproach:
### Brute-force and Backtracking Algorithm: <a href="https://github.com/Phbhan/Project-CNF-AI/blob/main/bruteforce.py"><strong>bruteforce.py</strong></a>
**Brute-force algorithm:**

&emsp;Step 1: Check whether all cells are assigned, if they are and the result satisfes the problem, return True and result matrix, else return False and an empty solution.

&emsp;Step 2: Get the current row and column index based on index parameter.

&emsp;Step 3: Try assigning current cell is red, then recursively call for the
next index. If the recursive call returns a solution, exit. Otherwise,
try assigning current cell is green, then recursively call for the next
index. It the call returns a solution, return that solution, else return
False as no solution is found.

**Backtracking algorithm:** The same as brute-force, but checking
whether the matrix conﬂicts with any constraints at every function
call, if it does, return False and exit the function call.
### CNF with A*:
#### Generate CNF clauses: <a href="https://github.com/Phbhan/Project-CNF-AI/blob/main/GenerateCNF.py"><strong>GenerateCNF.py</strong></a>
*Simple example*

Input matrix:

.|1|
---|---|
**.**|**.**|

Assign a Boolean variable to each cell like below:

A|B|
---|---|
**C**|**D**|

If a variable is True, then the corresponding cell is green, and vice versa.

We can state that: "Only 1 of these 4 cells is green", which is equivalent
to "Only 1 of these 4 variables is True".

First, we would have the constraint `(A ∨ B ∨ C ∨ D)` to make sure at least 1
of them is True.

Then, we build constraints to make sure there are at least 3 variables is
False:
* Assuming A is True, then B and C and D have to be False:

> A → ¬B ∧ ¬C ∧ ¬D

> ¬A ∨ (¬B ∧ ¬C ∧ ¬D)

> (¬A ∨ ¬B) ∧ (¬A ∨ ¬C) ∧ (¬A ∨ ¬D)

* Similarly, if B is True, then A and C and D is False: `(¬B ∨ ¬A) ∧ (¬B ∨ ¬C) ∧ (¬B ∨ ¬D)`
* The same for C: `(¬C ∨ ¬A) ∧ (¬C ∨ ¬B) ∧ (¬C ∨ ¬D)`
* The same for D: `(¬D ∨ ¬A) ∧ (¬D ∨ ¬B) ∧ (¬D ∨ ¬C)`

Combining all 4 cases, we have the constraints to make sure there are at
least 3 variables is False:

> (¬A ∨ ¬B) ∧ (¬A ∨ ¬C) ∧ (¬A ∨ ¬D) ∧ (¬C ∨ ¬A) ∧ (¬C ∨ ¬B) ∧ (¬C ∨ ¬D) ∧ (¬D ∨
¬A) ∧ (¬D ∨ ¬B) ∧ (¬D ∨ ¬C)

The entire express in CNF look like this, after removing all duplicate
clauses:

> (A ∨ B ∨ C ∨ D) ∧ (¬A ∨ ¬B) ∧ (¬A ∨ ¬C) ∧ (¬A ∨ ¬D) ∧ (¬B ∨ ¬C) ∧ (¬B ∨ ¬D) ∧ (¬C ∨ ¬D)

*A little more comlex example*

Input matrix:

**.**|**.**|**.**|
---|---|---|
**.**|8|**.**|
**.**|**.**|**.**|

The variable corresponding to each cell is:

A|B|C|
---|---|---|
**D**|**E**|**F**|
**G**|**H**|**I**|

The state is: “8 out of 9 variables are True, the other is False”.

Constraints to make sure there are at least 8 variables are True:

> (A ∨ B) ∧ (A ∨ C) ∧ (A ∨ D) ∧ (A ∨ E) ∧ (A ∨ F) ∧ (A ∨ G) ∧ (A ∨ H) ∧ (A ∨ I)
∧ (B ∨ C) ∧ (B ∨ D) ∧ (B ∨ E) ∧ (B ∨ F) ∧ (B ∨ G) ∧ (B ∨ H) ∧ (B ∨ I)
∧ (C ∨ D) ∧ (C ∨ E) ∧ (C ∨ F) ∧ (C ∨ G) ∧ (C ∨ H) ∧ (C ∨ I)
∧ (D ∨ E) ∧ (D ∨ F) ∧ (D ∨ G) ∧ (D ∨ H) ∧ (D ∨ I)
∧ (E ∨ F) ∧ (E ∨ G) ∧ (E ∨ H) ∧ (E ∨ I)
∧ (F ∨ G) ∧ (F ∨ H) ∧ (F ∨ I)
∧ (G ∨ H) ∧ (G ∨ I)
∧ (H ∨ I) **(1)**

Constraints to make sure there is at least 1 variable is False:

> ¬A ∨ ¬B ∨ ¬C ∨ ¬D ∨ ¬E ∨ ¬F ∨ ¬G ∨ ¬H ∨ ¬I **(2)**

Combine (1) and (2), we have the fnal CNF constraints for this example.

**Final principle:**

Let us call the value in the cell which we are building constraints is v, the
number of variables is n.
* Constraints to make sure there are at least v variables are True
is all positive combinations of `(n - v + 1)` variables of n variables.
* Constraints to make sure there are at least `(n – v)` variables are False is
all negative combinations of `(v + 1)` variables of n variables.

#### Using A* to solve CNF clauses: <a href="https://github.com/Phbhan/Project-CNF-AI/blob/main/Astart.py"><strong>Astart.py</strong></a>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;f(x) = g(x) + h(x)

f(x): The maximum number of satisfed clauses this state can lead to.

g(x): The number of satisfed clauses.

* The satisfed clause means that at least one of the variables of it is
True.

h(x): The number of non-conﬂict clauses.

The goal of this A* model is to assign the variables until all the clauses
are satisfed. Therefore, if g(x) equals to the number of CNF clauses,
we have reached the goal.

The conﬂict clauses appear in the unsatisfed clauses. 
E.g. (a, 0,0), (-a,0,0)

***The number of unsatisfed clauses = The number of non-conﬂict
clauses + The number of conﬂicts clauses.***

* The clauses in the satisfed clauses are already non-conﬂict, but we
do not mention it in the number of non-conﬂict clauses in the
above formula

##### Brieﬂy explain the algorithm: 

1. At each step, we pop the state in the priority queue. The state
indicates the assigned variable and its value.
    * The priority queue pops the element whose f(x) is largest, if
there are many elements having the same f(x), we choose the
largest g(x) one.
2. Assign value to the unassigned variable, calculate the f(x) as the
number of satisfed clauses plus the number of nonconﬂict clauses, and g(x) as the number of satisfed clauses. Add
the variable with the value to the state we got. Check if this state is
goal, if it is return the state, otherwise push it to the priority
queue.
3. Go to step 1.

##### The graph:

At each step, we can assign any unassigned variable.

E.g. We have to assign 3 variables (1, 2, 3) to solve the CNF.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![Figure](https://user-images.githubusercontent.com/62047983/162444956-4641389d-413a-45d6-b888-5eb72c20b0be.png)

In this example, 1, 2, 3 are the variables and 1, 0 are the values. At the
frst level, we assign each variable for each value and find the state
having the largest f(x), we choose variable 2 with value 1. At the second
level, we assign each unassigned variable with each value, choose the
state have the best f(x) in priority queue is variable 1 with value 0 and
continue until reach the goal. (Variable 3 with value 1 is not the goal but
the state (2:1, 1:0, 3:1))

At one variable, we have the connection to all other variables, so the
graph of relationship between each variables looks like:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![Figure](https://user-images.githubusercontent.com/62047983/162444963-f2a80746-4ff7-4448-bc1b-14b825d44e79.png)

However, assign by this way have the commutativity property. Mean that
if we assign (2:1, 1:0, 3:1) have the same meaning with (3:1, 2:1, 1:0) or
(3:1, 1:0, 2:1),... Also, the goal of us is solving all the CNF clauses without
considering reaching any specifc node. *Aware that the order of
assignment does not aﬀect the result*, we convert the graph to:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![Figure](https://user-images.githubusercontent.com/62047983/162445014-bdd7d631-8b71-48fd-b5e6-7d3898a82d11.png)

The graph of relationship between each variables looks like:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;![Figure](https://user-images.githubusercontent.com/62047983/162445025-96002ca4-5db7-4bef-8fe1-ded8e830a97e.png)

## Compare:
Input: The input is generated automatically by the function, then some
numbers are hidden manually

Result:

Input size | Time of A* | Time of Bactracking |
---|---|---|
5x5 | 0,082027 | 0,005475 |
9x9 | 18,94143 | 84,90632 |
10x10 | 1,422376 | 789,182741 |
11x11 | 36,83239 | 437,761719 |
15x15 | 119,627 | 1915,391263 |
20x20 | 184,109640 | Memory overﬂow |


![Figure](https://user-images.githubusercontent.com/62047983/162445037-49b94f90-8140-4d97-8c68-b246af60815c.png)

### Comment:
Backtracking:

* Easy to overﬂow memory for large test cases (> 15x15)
* The more numbers hidden in test cases (more "."), the longer the
backtracking runs.

A*:

* The larger g(x) may not lead to the solution.
* Our algorithm takes much time to calculate the heuristic, especially
counting the conﬂict clauses.
* In case the test case has many hidden numbers, which form large
arrays, A* may be "stuck" due to lack of basis to solve those
regions.

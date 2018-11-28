import numpy as np
from scipy.optimize import linprog

def printConstraint(c, b, n):
    for i in range(0, 2*n, 2):
        print("+" + str(int(c[i])) + "*a" + str(int(i/2 + 1)) + "^+ "
              + str(int(c[i+1])) + "*a" + str(int(i/2 + 1)) + "^⁻ ", end = '')
    print(" = " + str(b))

    return

def printConstraints(A_eq, b_eq, n):
    # Prints position constraint
    printConstraint(A_eq[0], b_eq[0], n)
    # Prints velocity constraint
    printConstraint(A_eq[1], b_eq[1], n)

    return

def main():
    t = 10
    time_increment = float(input('Enter the discretization interval: '))
    n = int(t/time_increment)

    # Constructing the coefficients vector of the objective function
    c = []
    for i in range(2*n):
        c.append(time_increment)

    # Constructing the equality constraints matrix
    A_eq = [[], []]
    b_eq = [1, 0]

    # Constructing the position constraint
    for i in range(0, 2*n, 2):
        ai = (10/time_increment + 1) - (i+1)/2
        A_eq[0].append(ai)
        A_eq[0].append(-ai)

    # Constructing the velocity constraint
    for i in range(0, 2*n, 2):
        A_eq[1].append(1)
        A_eq[1].append(-1)

    printConstraints(A_eq, b_eq, n)

main()

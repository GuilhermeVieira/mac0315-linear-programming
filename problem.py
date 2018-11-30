import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.optimize import linprog

def plotDiscretization(A, dx, title, xlabel, ylabel):
    x = 0
    # Create figure and axes
    fig, ax = plt.subplots(1)
    plt.ylim([-dx, dx])
    plt.xlim([0,10])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    for i in range(len(A)):
        if A[i] >= 0:
            rect = Rectangle((x,0), dx, A[i],linewidth=1,edgecolor='r',facecolor='none')
        # Add the patch to the Axes
        else:
            rect = Rectangle((x,A[i]), dx, -A[i],linewidth=5,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
        x = x + dx
    plt.show()

    return

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

def findAccelerations(x, n):
    A = []
    for i in range(0,n, 2):
        A.append(x[i] - x[i+1]) # xi = xi^+ - xi^-
    return A

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

    # Constructing bound variables
    bounds = ()
    for i in range (2*n):
        bounds = bounds + ((0, None), )

    printConstraints(A_eq, b_eq, n)
    print(bounds)
    res = linprog(c, A_eq= A_eq, b_eq=b_eq, bounds=bounds, options={"disp": True})
    # Adding the values of a0^+ and a0^-
    x = [0, 0]
    for i in range(2*n):
        x.append(res.x[i])

    print(res)

    A = findAccelerations(x, 2*n + 2)
    print(A)

    plotDiscretization(A, time_increment, "Acceleration Graph", "Time", "Acceleration")
main()

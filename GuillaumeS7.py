from pycsp3 import *

# letters[i] is the digit of the ith letter involved in the equation
s, e, n, d, m, o, r, y = letters = VarArray(size=8, dom=range(10))

satisfy(
    # letters are given different values
    AllDifferent(letters),

    # words cannot start with 0
    [s > 0, m > 0],

    # respecting the mathematical equation
    [s, e, n, d] * [1000, 100, 10, 1]
    + [m, o, r, e] * [1000, 100, 10, 1]
    == [m, o, n, e, y] * [10000, 1000, 100, 10, 1]
)
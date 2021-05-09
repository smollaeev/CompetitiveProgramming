import numpy as np
def calculate_MaxNumber (A, n, x):
    numberOfUniques = len (np.unique (A))
    if n - numberOfUniques < x:
        return numberOfUniques - (x - n + numberOfUniques)
    else:
        return numberOfUniques

T = int (input ())
for t in range (T):
    firstLine = input ().split ()
    firstLineInt = list (map (int, firstLine))
    n = firstLineInt [0]
    x = firstLineInt [1]
    secondLine = input ().split ()
    A = list (map (int, secondLine))
    print (calculate_MaxNumber (A, n, x))
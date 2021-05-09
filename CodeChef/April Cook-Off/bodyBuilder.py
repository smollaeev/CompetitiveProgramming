def calculate_TheMaxTension (N, B, A, R):
    x = 0
    tensions = []
    for i in range (N):
        x += B [i]
        tensions.append (x)
        if i != (N - 1):
            x -= ((A [i + 1] - A[i]) * R)
            x = max (0, x)
    return max (tensions)

T = int (input ())
for t in range (T):
    firstLine = input ().split ()
    intInput = list (map (int, firstLine))
    N = intInput [0]
    R = intInput [1]
    secondLine = input ().split ()
    A = list (map (int, secondLine))
    thirdLine = input ().split ()
    B = list (map (int, thirdLine))
    print (calculate_TheMaxTension (N, B, A, R))
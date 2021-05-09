def can_Reach (x, y, xR, yR, D):
    if xR * D <= x and yR * D <= y:
        return True
    else:
        return False
T = int (input ())
for t in range (T):
    input_ = input ().split ()
    x = int (input_ [0])
    y = int (input_ [1])
    xR = int (input_ [2])
    yR = int (input_ [3])
    D = int (input_ [4])
    if can_Reach (x, y, xR, yR, D):
        print ('YES')
    else:
        print ('NO')
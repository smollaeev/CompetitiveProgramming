def can_Escape (x, y):
    while (x != N or y != M):
        
T = int (input ())
for t in range (T):
    firstLine = input ().split ()
    N = int (firstLine [0])
    M = int (firstLine [1])
    secondLine = input ().split ()
    x = int (secondLine [0])
    y = int (secondLine [1])
    thirdLine = input ().split ()
    a = thirdLine [0]
    b = thirdLine [1]
    if can_Escape (x, y,):
        print ('YES')
    else:
        print ('NO')
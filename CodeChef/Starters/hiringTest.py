def determine_Result (results, X, Y):
    full = 0
    partial = 0
    for r in range (len (results)):
        if results [r] == 'F':
            full += 1
        else:
            if results [r] == 'P':
                partial += 1
    if (full >= X) or (full == X - 1 and partial >= Y):
        return 1
    else:
        return 0

T = int (input ())
for t in range (T):
    firstLine = input ().split ()
    N = int (firstLine [0])
    M = int (firstLine [1])
    secondLine = input ().split ()
    X = int (secondLine [0])
    Y = int (secondLine [1])
    answer = []
    for i in range (N):
        results = input ()
        answer.append (determine_Result (results, X, Y))
    print (''.join(map(str, answer)))
def is_Consistent (type, i , j, N):
    HorP = []
    for n in range (N):
        HorP.append ('None')
    while ():
        

T = int (input ())
if T<1 or T>100000:
    exit ()
answers = []
for t in range (T):
    firstLineList = input ().split ()
    if len (firstLineList) != 2:
        exit ()
    N = firstLineList [0]
    if N<1 or N>500000:
        exit ()
    Q = firstLineList [1]
    if Q<0 or Q> min [2*N*(N-1), 1000000]:
        exit ()
    type = []
    i = []
    j = []
    for q in range (Q):
        queryList = input ().split ()
        if len (queryList) != 3:
            exit ()
        type.append (int (queryList [0]))
        if type (q)<1 or type (q)> 2:
            exit ()
        i.append (int (queryList [1]))
        j.append (int (queryList [2]))
        if i < 1 or i>N or j < 1 or j>N or i == j:
            exit ()
    if not (is_Consistent (type, i , j, N)):
        answers.append (-1)
    else:
        answers.append (calculate_MaximumParasites ())

for t in range (T):
    print (answers [t])
    
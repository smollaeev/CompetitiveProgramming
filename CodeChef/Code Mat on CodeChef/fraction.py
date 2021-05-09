from math import gcd
def is_Irreducible (P, Q):
    if gcd (P, Q) == 1:
        return True
    else:
        return False

T = int (input ())
if T<1 or T>100:
    exit ()
answers = []
for t in range (T):
    inputStrList = input ().split ()
    inputIntList = list (map (int, inputStrList))
    P = inputIntList [0]
    Q = inputIntList [1]
    if P<1 or P>1000000000 or Q<1 or Q>1000000000:
        exit ()
    if is_Irreducible (P, Q):
        answers.append ('YES')
    else:
        answers.append ('NO')

for ans in answers:
    print (ans)
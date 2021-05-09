def calculate_TotalDistance (X, K, P, fullOrEmpty):
    district = X - 1
    n = 1
    while fullOrEmpty [district] == 'Full' and district < len (P):
        district += 1
        n += 1
    d = K - P [district]
    if d >= 0:
        fullOrEmpty [district] = 'Full'
    i = 1
    if district >= len (P):
        return [0, fullOrEmpty]
    numberOfPeople = 0
    while d > 0 and district < len (P):
        try:
            d = d - P [district + i]
            if d >= 0:
                fullOrEmpty [district + i] = 'Full'
                K -= P [district + i]
                numberOfPeople += (K - d)
            else:
                P [district + i] = abs (d)
            i += 1
        except:
            return [numberOfPeople * (i - 1), fullOrEmpty]
    return [numberOfPeople * (i - 1), fullOrEmpty]

N = int (input ())
if N <1 or N > 100000:
    exit ()
inputStr = input ()
inputStrList = inputStr.split ()
if len (inputStrList) != N:
    exit ()
P = list (map (int, inputStrList))
for p in P:
    if p < 1 or p > 1000000000:
        exit ()
Q = int (input ())
if Q<1 or Q> 100000:
    exit ()

X = []
K = []

fullOrEmpty = []
for p in range (N):
    fullOrEmpty.append ('Empty')

totalDistances = []
for q in range (Q):
    inputStr = input ()
    inputStrList = inputStr.split ()
    if len (inputStrList) != 2:
        exit ()
    query = list (map (int, inputStrList))
    if query [0] <1 or query [0]> N:
        exit ()
    if query [1]<1 or query [1]>1000000000:
        exit ()
    X.append (query [0])
    K.append (query [1])

for q in range (Q):
    distancesAndCapacities = calculate_TotalDistance (X [q],K[q],P, fullOrEmpty)
    totalDistances = distancesAndCapacities [0]
    fullOrEmpty = distancesAndCapacities [1]
    print (totalDistances)
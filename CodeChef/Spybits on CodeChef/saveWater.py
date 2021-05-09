def is_Possible (H, x, y, C):
    if H* (x + int (y / 2)) <= C:
        return True
    else:
        return False


T = int (input ())
if T<1 or T > 300:
    exit ()
ans = []
for t in range (T):
    inputStr = input ()
    inputStrList = inputStr.split ()
    if len (inputStrList) != 4:
        exit ()
    inputIntList = list (map(int, inputStrList))
    for i in range (3):
        if inputIntList [i]<1 or inputIntList [i] > 10:
            exit ()
    if inputIntList [3] <1 or inputIntList [3] > 100:
        exit ()
    H = inputIntList [0]
    x = inputIntList [1]
    y = inputIntList [2]
    C = inputIntList [3]

    if is_Possible (H, x, y, C):
        ans.append ('YES')
    else:
        ans.append ('NO')

for t in range (T):
    print (ans[t])

def passOrFail (input_):
    for i in range (4, 7):
        if input_ [i] < input_ [i-4]:
            return 'NO'
    if sum (input_ [4:]) < input_[3]:
        return 'NO'
    return 'YES'

T = int (input ())
if T<1 or T> 100:
    exit ()
answers = []
for t in range (T):
    inputStrList = input().split ()
    inputIntList = list (map (int, inputStrList))
    if len (inputIntList) != 7:
        exit ()
    for i in range (7):
        if i != 3:
            if inputIntList [i]< 1 or inputIntList [i]>100:
                exit ()
    lst = inputIntList [:3]
    # if (sum (inputIntList[:3]) > inputIntList [3]) or inputIntList [3]>300:
    #     exit ()
    answers.append (passOrFail (inputIntList))

for t in range (T):
    print (answers [t])
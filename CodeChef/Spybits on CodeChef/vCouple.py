from itertools import permutations

def calculate_MinimumMaximumLikeness (heightOfBoys, heightOfGirls):
    # uniqueCombinations = []
    heightOfBoys.sort ()
    heightOfGirls.sort (reverse = True)
    # permut = permutations (heightOfBoys, len(heightOfGirls))
    # for comb in permut:
    #     zipped = zip(comb, heightOfGirls)
    #     uniqueCombinations.append(list(zipped))   

    # maximums = []
    # for set in uniqueCombinations:
    #     likenesses = []
    #     for tup in set:
    #         likenesses.append (sum (tup))
    #     maximums.append (max (likenesses))
    likenesses = [heightOfGirls [i]+heightOfBoys[i] for i in range (len (heightOfBoys))]
    return max (likenesses)

T = int (input ())
if T <1 or T > 5:
    exit ()
minimumMaximumLikeness = []
for t in range (T):
    N = int (input ())
    if N <1 or N > 20000:
        exit ()
    inputStr = input ()
    inputStrList = inputStr.split ()
    if len (inputStrList) != N:
        exit ()
    heightOfBoys = list (map (int, inputStrList))
    for a in heightOfBoys:
        if a < 1 or a > 1000000000:
            exit ()
    inputStr = input ()
    inputStrList = inputStr.split ()
    if len (inputStrList) != N:
        exit ()
    heightOfGirls = list (map (int, inputStrList))
    for b in heightOfGirls:
        if b <1 or b> 1000000000:
            exit ()
    minimumMaximumLikeness.append (calculate_MinimumMaximumLikeness (heightOfBoys, heightOfGirls))

for t in range (T):
    print (minimumMaximumLikeness [t])

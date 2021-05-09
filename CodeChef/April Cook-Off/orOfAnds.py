import numpy as np
def find_SubArrays (arr, start, end, result):
    # results = []
    # for i in range(0,n):
    #     for j in range(i,n):
    #         result = []
    #         for k in range(i,j+1):
    #             result.append (arr [k])
    #         results.append (result)
    # return (results)
    if end == len(arr):
        return result  
    # Increment the end point and start from 0
    elif start > end:
        return find_SubArrays(arr, 0, end + 1, result)          
    # Print the subarray and increment the starting
    # point
    else:
        result.append (arr[start:end + 1])
        return find_SubArrays(arr, start + 1, end, result)

def calculate_Answer (arr):
    subArrays = find_SubArrays (arr, 0, 0, [])
    scores = []
    for subArray in subArrays:
        scores.append (np.bitwise_and.reduce (subArray))
    return np.bitwise_or.reduce (scores)

T = int (input ())
for t in range (T):
    firstLine = input ().split ()
    N = int (firstLine [0])
    Q = int (firstLine [1])
    secondLine = input ().split ()
    A = list (map (int ,secondLine))
    print (calculate_Answer (A))

    for q in range (Q):
        line = input ().split()
        X = int (line [0])
        V = int (line [1])
        A [X - 1] = V
        print (calculate_Answer (A))
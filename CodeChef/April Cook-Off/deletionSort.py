import copy
def find_SubArrays (arr, start, end, result):
    if end == len(arr):
        return result  
    # Increment the end point and start from 0
    elif start > end:
        return find_SubArrays(arr, 0, end + 1, result)          
    # Print the subarray and increment the starting
    # point
    else:
        if len (arr[start:end + 1]) == 2:
            result.append (arr[start:end + 1])
        return find_SubArrays(arr, start + 1, end, result)

def calculate_NumberOfGoods (subArrays, A):
    count = 0
    for i in range (len (subArrays)):
        remove_ = []
        for j in subArrays [i]:
            remove_.append (j)
        try:
            arr = copy.deepcopy (A)
            for r in range (remove_ [0], remove_ [1]):
                m = arr[r]
                while arr:
                    arr.remove(m)
        except ValueError:
            pass
        if arr == sorted (arr):
            count += 1
    return count
T = int (input ())
for t in range (T):
    N = int (input ())
    secondLine = input ().split()
    A = list (map (int, secondLine))
    indices = list (range (0, len (A)))
    subArrays = find_SubArrays (indices, 0, 0, [])
    print (calculate_NumberOfGoods (subArrays, A))
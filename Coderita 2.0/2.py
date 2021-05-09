#User function Template for python3
import numpy as np
from numpy.core.numeric import indices
class Solution:
    def maxSum(self, N, A): 
        #code here
        result = 0
        subArrays = []
        copy_ = A
        copy_ = sorted(copy_)
        print (copy_)
        if N > 1:
            if (copy_ [0] < 0) and (copy_ [1] < 0):
                A[A.index (copy_ [0])] = A[A.index (copy_ [0])] * -1
                A[A.index (copy_ [1])] = A[A.index (copy_ [1])] * -1
            subArrays = [A [i: j] for i in range(N) for j in range(i + 1, N + 1)] 
            for i in range (len (subArrays)):
                result += sum (subArrays [i])
            return result
        else:
            return abs (A [0])
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxSum(N, A)
        print(ans)
# } Driver Code Ends
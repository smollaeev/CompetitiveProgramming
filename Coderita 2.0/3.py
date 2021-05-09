#User function Template for python3
class Solution:
    def maximumBeauty(self, N, K, B):
        # code here   
        if N/K < 1:
            return 0
        else:
            sublists = []
            for i in range (N):
                sublists.append (B [i])
                m = i
                while (len (sublists [i]) < K):
                    try:
                        m += + 2
                        sublists [i].append ([B [m]])
                    except:
                        break
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(1000000)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,K = map(int,input().strip().split())
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maximumBeauty(N, K, B)
        print(ans)
# } Driver Code Ends
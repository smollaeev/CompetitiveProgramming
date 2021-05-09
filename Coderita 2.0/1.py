#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        #code here
        ans=0
        for i in range(len(S)):
            c=0
            for j in range(i,len(S)):
                if ord(S[j])>=ord('a') and ord(S[j])<=ord('z'):
                    c+=1
                else:
                    c-=1
                if c==0:
                    ans+=1
        return ans
#{ 
#Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

#} Driver Code Ends
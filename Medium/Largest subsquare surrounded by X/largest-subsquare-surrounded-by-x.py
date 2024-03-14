#User function Template for python3
class Solution:
    def largestSubsquare(self, n, a):
        #code here
        r,c=len(a),len(a[0])
        dp=[[[0,0]for _ in range(r+1)]for _ in range(c+1)]
        for i in range(r):
            for j in range(c):
                if a[i][j]=="X":
                    dp[i+1][j+1][0]=1+dp[i][j+1][0]
                    dp[i+1][j+1][1]=1+dp[i+1][j][1]
        mx=0
        for i in range(r,0,-1):
            for j in range(c,0,-1):
                mn=min(dp[i][j][0],dp[i][j][1])
                while mn>mx:
                    if dp[i-mn+1][j][1]>=mn and dp[i][j-mn+1][0]>=mn:
                        mx=mn
                    else:
                        mn=mn-1
        return mx
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends
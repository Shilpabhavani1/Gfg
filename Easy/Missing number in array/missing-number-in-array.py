class Solution:
    def missingNumber(self,a,n):
        # code here
        s=0
        for i in range(len(a)):
            s+=a[i]
        na=n*(n+1)//2
        c=abs(na-s)
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends
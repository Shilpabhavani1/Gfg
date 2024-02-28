#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        s=s[-3:]
        s=int(s)
        if s%8==0:
            return 1
        return -1
        # n=list(s)
        # l=[]
        # if len(l)<3:
        #     if (int(s)%8)==0:
        #         return 1
        # else:
        #     l.append(n[-1])
        #     l.append(n[-2])
        #     l.append(n[-3])
        #     i=int(l)
        #     if i%8==0:
        #         return 1
        # return -1
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends
#User function Template for python3
import re
class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        l=0
        n=len(s)
        mod=10**9+7
        ab=0
        for i in range(n):
            val=int(s[i])
            ab=((ab*10)+val*(i+1))%mod
            l=(l+ab)%mod
        return l
    
    
    # def sumSubstrings(self,s):
        
    #     # code here
    #     # l=[int(i) for i in str(s)]
    #     k=[]
    #     l=[]
    #     # print(l)
    #     for i in range(len(s)):
    #         for j in range(i+1,len(s)+1):
    #             # print(l[i:j+1])
    #             k.append(re.sub(r'\W+', '', s[i:j]))
    #     # print(k)
    #     for i in range(len(k)):
    #         l.append(int(k[i]))
    #     # print(sum(l))
    #     return sum(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends
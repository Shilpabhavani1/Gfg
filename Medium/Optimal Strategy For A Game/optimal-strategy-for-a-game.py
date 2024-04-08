#User function Template for python3


#Function to find the maximum possible amount of money we can win.
from functools import lru_cache
import sys
#Function to find the maximum possible amount of money we can win.
sys.setrecursionlimit(10**6)
class Solution:
    def optimalStrategyOfGame(self,n, arr):
        @lru_cache(None)
        def dfs(i,j,case):
            if i>j:
                return 0
            if case:
                return max(arr[i]+dfs(i+1,j,not case),arr[j]+dfs(i,j-1,not case))
            return min(dfs(i+1,j,not case),dfs(i,j-1,not case))
        return dfs(0,n-1,True)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends
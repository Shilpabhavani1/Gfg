#User function Template for python3
class Solution:

	
	def sumBitDifferences(self,arr, n):
	    result=0
	    for i in range(32):
	        setBits=0
	        unsetBits=0
	        for num in arr:
	            if num &(1 << i):
	                setBits+=1
	            else:
	                unsetBits+=1
	        
	        result+=setBits*unsetBits*2
	   
	    return result
    	# code here



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
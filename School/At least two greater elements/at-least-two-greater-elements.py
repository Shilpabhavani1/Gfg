#User function Template for python3

class Solution:
    def findElements(self,a, n):
        # Your code goes here
        a.sort()
        return a[:-2]
        # a.remove(max(a))
        # for i in range(len(a)-1):
        #     if a[i]>a[i+1]:
        #         a[i],a[i+1]=a[i+1],a[i]
        # a.remove(max(a))
        # return a
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n = int(input())
    	a = [int(x) for x in input().strip().split()]
    	ob=Solution()
    	print(*ob.findElements(a, n))
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends
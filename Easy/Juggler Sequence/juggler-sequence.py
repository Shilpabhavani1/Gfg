#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        lst=[n]
        while lst[-1]!=1:
            if lst[-1]&1:
                lst.append(int((lst[-1])**(3/2)))
            else:
                lst.append(int((lst[-1])**(1/2)))
        return lst
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends
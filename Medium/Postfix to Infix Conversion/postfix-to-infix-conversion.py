#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        s=[]
        for i in postfix:
            if i.isalpha():
                s.append(i)
            else:
                a=s.pop()
                b=s.pop()
                s.append("("+b+i+a+")")
        return s[-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToInfix(postfix)
        print(res)
# } Driver Code Ends
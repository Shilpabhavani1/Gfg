#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        s=[]
        res=""
        for i in range(len(pre_exp)-1,-1,-1):
            c=pre_exp[i]
            if c.isalpha():
                s.append(c)
            else:
                a=s.pop()
                b=s.pop()
                res="("+a+c+b+")"
                s.append(res)
        return s[-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToInfix(prefix)
        print(res)
# } Driver Code Ends
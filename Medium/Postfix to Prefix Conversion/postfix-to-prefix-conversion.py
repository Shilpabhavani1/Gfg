#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        s=[]
        for i in post_exp:
            if i.isalpha():
                s.append(i)
            else:
                a=s.pop()
                b=s.pop()
                s.append(i+b+a)
        return s[0]
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToPre(postfix)
        print(res)
# } Driver Code Ends
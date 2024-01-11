#User function Template for python3

class Solution:

    def removeKdigits(self, l, K):
        # code here
        stack = []
        for digit in S:
            while K > 0 and stack and stack[-1] > digit:
                stack.pop()
                K -= 1
            stack.append(digit)
        while K > 0:
            stack.pop()
            K -= 1
        result = ''.join(stack).lstrip('0')
        return result if result else '0'
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends
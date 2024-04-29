#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        operators=["+","-","*","/","^","(",")"]
        precedance={"+":1,"-":1,"*":2,"/":2,"^":3}
        stack=[]
        output=""
        for ch in exp:
            if ch not in operators:
                output+=ch
            elif ch=="(":
                stack.append(ch)
            elif ch==")":
                while stack and stack[-1]!="(":
                    output+=stack.pop()
                stack.pop()
            else:
                while stack and stack[-1]!="(" and precedance[ch]<=precedance[stack[-1]]:
                    output+=stack.pop()
                stack.append(ch)
        while stack:
            output+=stack.pop()
        return output


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends
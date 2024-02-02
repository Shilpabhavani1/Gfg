#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        # for i in s:
        #     if i.isalpha():
        #         return -1
        # return int(s)
        for i in range(len(s)):
            if i!=0 and s[i]=="-":
                return -1
            if s[i].isalpha():
                return -1
        return int(s)


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        if pat not in txt:
            return [-1]
        n=len(pat)
        i=0
        j=n
        p=[]
        while(i<j and i<len(txt)):
            if txt[i:j]==pat:
                p.append(i+1)
            i=i+1
            j=j+1
        return p
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends
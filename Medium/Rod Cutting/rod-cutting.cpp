//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution{
  public:
  int dp[10001];
  int fun(int price[],int n)
  {
      if(n==0) return 0;
      if(dp[n]!=-1) return dp[n];
      int ans=INT_MIN;
      for(int i=0;i<n ;i++)
      {
          int len=i+1;
          int sub=price[i]+fun(price,n-len);
          ans=max(ans,sub);
      }
      return dp[n]=ans;
      
  }
  
  
  
    int cutRod(int price[], int n) {
        //code here
        memset(dp,-1,sizeof(dp));
        return fun(price,n);
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) 
            cin >> a[i];
            
        Solution ob;

        cout << ob.cutRod(a, n) << endl;
    }
    return 0;
}
// } Driver Code Ends
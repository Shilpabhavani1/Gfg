//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
    public:
    void Fun(int i,int j, int n,vector<vector<int>>&m,vector<string>&v,string s)
    {
        if(i<0 or j<0 or i>=n or j>=n)
        {
            return;
        }
        if(m[i][j]==0 or m[i][j]==-1)
        {
            return;
        }
        if(i==n-1 and j==n-1)
        {
            v.push_back(s);
        }
        m[i][j]=-1;
        Fun(i+1,j,n,m,v,s+"D");
        Fun(i,j+1,n,m,v,s+"R");
        Fun(i-1,j,n,m,v,s+"U");
        Fun(i,j-1,n,m,v,s+"L");
        m[i][j]=1;
    }
    
    
    
    
    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here
        string s;
        vector<string> v;
        Fun(0,0,n,m,v,s);
        return v;
    }
};

    


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends
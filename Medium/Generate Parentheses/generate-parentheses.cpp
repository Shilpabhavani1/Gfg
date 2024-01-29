//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;
vector<string> AllParenthesis(int n) ;


// } Driver Code Ends
//User function Template for C++

// N is the number of pairs of parentheses
// Return list of all combinations of balanced parantheses
class Solution
{
    public:
    void fun(int o,int c,int n,string &s,vector<string>&v)
    {
        if(n==o and n==c)
        {
            v.push_back(s);
            return;
        }
        if(o<n)
        {
            s=s+"(";
            fun(o+1,c,n,s,v);
            s.pop_back();
        }
        if(o>c)
        {
            s=s+")";
            fun(o,c+1,n,s,v);
            s.pop_back();
        }
    }
    
    vector<string> AllParenthesis(int n) 
    {
        // Your code goes here 
        string s;
        vector<string>v;
        fun(0,0,n,s,v);
        return v;
    }
};

//{ Driver Code Starts.


int main() 
{ 
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		Solution ob;
		vector<string> result = ob.AllParenthesis(n); 
		sort(result.begin(),result.end());
		for (int i = 0; i < result.size(); ++i)
			cout<<result[i]<<"\n";
	}
	return 0; 
} 

// } Driver Code Ends
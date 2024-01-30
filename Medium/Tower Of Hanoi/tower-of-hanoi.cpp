//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // You need to complete this function

    // avoid space at the starting of the string in "move disk....."
    void MoveDisk(int N,int scr,int des,int help,long long &cnt)
    {
        if(N>0)
        {
            MoveDisk(N-1,scr,help,des,cnt);
            cout<<"move disk "<<N<<" from rod "<<scr<<" to rod "<<des<<endl;
            cnt++;
            MoveDisk(N-1,help,des,scr,cnt);
        }
    }
    
    
    long long toh(int N, int scr, int des, int help) {
        
        // Your code here
        long long cnt=0;
        MoveDisk(N,scr,des,help,cnt);
        return cnt;
    }
};

//{ Driver Code Starts.

int main() {

    int T;
    cin >> T;//testcases
    while (T--) {
        
        int N;
        cin >> N;//taking input N
        
        //calling toh() function
        Solution ob;
        
        cout << ob.toh(N, 1, 3, 2) << endl;
    }
    return 0;
}



// } Driver Code Ends
//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
  
  int node_ans=-1;
  
  int bfs(int st,vector<pair<int,int>>adj[],int n,int m,int th){
      
      vector<int> dist(n,INT_MAX);
      dist[st]=0;
      queue<int> q;
      q.push(st);
      int count=0;
      
      while(!q.empty()){
          
          int node= q.front();
          q.pop();
          
          for(auto it : adj[node]){
              
              int n1= it.first;
              int wt= it.second;
              
              if(dist[n1]> dist[node]+wt){
                  dist[n1]= dist[node]+wt;
                  q.push(n1);
                }
           }
        }
        for(int i=0;i<n;i++){
            
            if(dist[i]!=0){
                
                if(dist[i]<=th){
                    count++;
                }
            }
        }
        return count;
        
        
      
  }
    int findCity(int n, int m, vector<vector<int>>& edges, int distanceThreshold) {
        
        vector<pair<int,int>> adj[n];
        
        for(int i=0;i<m;i++){
            
            adj[edges[i][0]].push_back({edges[i][1],edges[i][2]});
            adj[edges[i][1]].push_back({edges[i][0],edges[i][2]});
        }
        
        int ans=INT_MAX;
        
        for(int i=0;i<n;i++){
            
            
            int reachable_node= bfs(i,adj,n,m,distanceThreshold);
            
            if(ans>=reachable_node){
                ans=reachable_node;
                node_ans=i;
            }
            
            
        }
        return node_ans;
        // Your code here
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> adj;
        // n--;
        for (int i = 0; i < m; ++i) {
            vector<int> temp;
            for (int j = 0; j < 3; ++j) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }

        int dist;
        cin >> dist;
        Solution obj;
        cout << obj.findCity(n, m, adj, dist) << "\n";
    }
}

// } Driver Code Ends
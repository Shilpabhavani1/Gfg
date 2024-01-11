//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node 
{
    int data;
    struct Node *next;
    
    Node(int x) {
        data = x;
        next = NULL;
    }
};

// function to display the linked list
void display(Node* head)
{
	while (head != NULL) {
		cout << head->data << " ";
		head = head->next;
	}
	cout<<endl;
}

Node* insertInMiddle(Node* head, int x);

int main()
{
    int T, n, x;
    cin>>T;
    while(T--)
    {
        cin>> n >> x;
        
        struct Node *head = new Node(x);
        struct Node *tail = head;
        
        for (int i=0; i<n-1; i++)
        {
            cin>>x;
            tail->next = new Node(x);
            tail = tail->next;
        }
        
        cin>> x;
        head = insertInMiddle(head, x);
        display(head);
    }
    return 0;
}

// } Driver Code Ends


/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/

//Function to insert a node in the middle of the linked list.
Node* insertInMiddle(Node* head, int x)
{
// 	// Code here
    Node* p=new Node(x);
    if(head==NULL) return p;
    int c=1;
    Node* t=head;
    while(t->next!=NULL)
    {
        t=t->next;
        c++;
    }
    int i=1;
    t=head;
    int k;
    if(c%2!=0)
    {
        k=(c/2)+1;
    }
    else
    {
        k=c/2;
    }
    while(i<k)
    {
        t=t->next;
        i++;
    }
    Node* temp=t->next;
    t->next=p;
    p->next=temp;
    return head;
}









// 	Node* p=new Node(x);
// 	if(head==NULL) return p;
// 	Node* t=head;
// 	Node* r=head;
// 	while(r!=NULL and r->next!=NULL)
// 	{
// 	    t=t->next;
// 	    r=r->next->next;
// 	}
// 	if(r!=NULL)
// 	{
// 	    r=t->next;
// 	    t->next=p;
// 	    p->next=r;
// 	}
// 	else
// 	{
// 	    r=head;
// 	    if(r->next!=t)
// 	    {
// 	        r=r->next;
// 	    }
// 	    r->next=p;
// 	    p->next=t;
// 	}
// 	return head;

//   Node* p=new Node(x);//Insertion at first
//   p->next=head;
//   return p;

//     Node* p=new Node(x);//Insertion at End
//     Node* temp=head;
//     while(temp->next!=NULL)
//     {
//         temp=temp->next;
//     }
//     temp->next=p;
//     return head;
// }
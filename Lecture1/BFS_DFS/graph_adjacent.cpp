#include <iostream>
#include <vector>
#include <queue>
using namespace std; 

vector <int> adj[10];
int level[10];
bool visited[10];
int distance[10];

void bfs(int s)
{
	queue <int> q;
	q.push(s);
	level[s] = 0;
	visited[s] = true;


	while(!q.empty())
	{
		int p = q.front();
		q.pop();
		for(int i = 0; i < adj[p].size(); i++)
		{
			if (visited[adj[p][i]] == false)
			{
				level[adj[p][i]] = level[p] + 1;
				q.push(adj[p][i]);
				visited[adj[p][i]] = true;
			}
		}
	}
}


void bfs2(int start)
{
	deque <int> Q;  //Double-ended queue
	Q.push_back(start);
	distance[start] = 0;
	while(!Q.empty())
	{
		int p = Q.front();
		Q.pop_front();
		for(int i = 0; i < edges[p].size(); i++)
		{
			
		}
	}

}
int main()
{
	int x, y, nodes, edges;
	int start = 0; 
	cin >> nodes; 
	cin >> edges; 
	//cin >> start;
	for(int i = 0; i < edges; i++)
	{
		cin >> x >> y;
		adj[x].push_back(y);
		adj[y].push_back(x);

	}

	for(int i = 1; i <= nodes; i++)
	{
		cout << "Adjacent list of node " << i << ": ";	
		for(int j = 0; j < adj[i].size(); j++)
		{
			if (j == adj[i].size() - 1)
			{
				cout << adj[i][j] << endl;
			}
			else 
			{
				cout << adj[i][j] << " --> ";
			}
		}
	}

	bfs(start);

	for(int i = 0; i <= nodes; i++)
	{
		cout << "Node " << i << " is at level " << level[i]	 << endl;
	}
	return 0;
}

#include <iostream>
#include <vector>
#include <queue>
using namespace std;


const int MAX = 100;
vector <int> graph[MAX];
bool visited[MAX];
int path[MAX];
int V, E;
int level[MAX];

void bfs(int start)
{
	int v;
	for(int i = 0; i <= V; i++)
	{
		visited[i] = false;
		path[i] = -1;
	}
	queue <int> q;
	visited[start] = true;
	q.push(start);
	level[start] = 0;

	while (!q.empty())
	{
		v = q.front();
		q.pop();
		for(int i = 0; i < graph[v].size(); i++)
		{
			if (visited[graph[v][i]] == false) 
			{
				visited[graph[v][i]] = true;
				q.push(graph[v][i]);
				path[graph[v][i]] = v;
				level[graph[v][i]] = level[v] + 1;
			}
		
		}
	}
}


void printPath(int start,int destination)
{
	vector <int> b;
	if (destination == start)
	{
		cout << destination << endl;
		return;	
	}

	if (path[destination] == -1)
	{
		cout << "No path" << endl;
		return;
	}
	while(true)
	{
		b.push_back(destination);
		destination = path[destination];
		if (destination == start)
		{
			b.push_back(start);
			break;	
		}
	}

	for(int i = b.size() - 1; i > -1; i--)
	{
		cout << b[i] << " ";
	}
	cout << "\n" ;

}

int main()
{
	int u, v;
	int start, destination;
	cin >> V;
	cin >> E;
	for(int i = 0; i < E; i++)
	{
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	for(int i = 1; i <= V; i++)
	{
		cout << "Adjacent nodes of node " << i << " : ";
		for(int j = 0; j < graph[i].size(); j++)
		{
			if (j == graph[i].size() - 1) 
			{
				cout << graph[i][j] << endl;
			}

			else 
			{
				cout << graph[i][j] << " and ";
			}
		
		}
		
	}

	start = 1;
	destination = 7;
	bfs(start);
	for(int i = 1; i <= V; i++)
	{
		cout << "Level of node " << i << " is " << level[i]	 << endl;
	}
	cout << "Path from " << start << " to " << destination << endl;
	printPath(start, destination);

	return 0;
}

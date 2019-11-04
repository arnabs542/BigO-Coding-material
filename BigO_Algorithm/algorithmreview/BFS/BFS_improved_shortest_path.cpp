#include<iostream>
#include <list>
#include <queue>
using namespace std;
#define MAX 1005
int V, E;
bool visited[MAX];
int path[MAX];
list<int> graph[MAX];
int dist[MAX]; 
 
void BFS(int s)
{
	for (int i = 1; i <= V; i++)
	{
		visited[i] = false;
		path[i] = -1;
		dist[i] = -1; 
	}
	queue<int> q;
 
	visited[s] = true;
	q.push(s);
	dist[s] = 0; 
 
	list<int>::iterator i;
 
	while (!q.empty())
	{
		s = q.front();
		q.pop();
		for (i = graph[s].begin(); i != graph[s].end(); i++)
		{
			if (!visited[*i])
			{
				visited[*i] = true;
				dist[*i] = dist[s] + 1; 
				q.push(*i);
				path[*i] = s;
			}
		}
	}
}
 
int countPath(int s, int f, int back[])
{
 
	int count = 0;
	int b[MAX];
	int m = 0;
	if (back[f] == -1)
		return -1;
	while (1)
	{
		b[m++] = f;
		f = back[f];
		if (f == s)
		{
			b[m++] = s;
			break;
		}
	}
	for (int i = m - 1; i >= 0; i--)
	{
		if (b[i] > 0)
			count++;
	}
	return count-1;
}
 
int main()
{
	//freopen("INPUT.INP", "rt", stdin);
	//freopen("OUTPUT.OUT", "wt", stdout);
	int u, v, q, s;
	cin >> q;
	while (q--)
	{
		cin >> V;
		cin >> E;
		for (int i = 0; i < E; i++)
		{
			cin >> u >> v;
			graph[u].push_back(v);
			graph[v].push_back(u);
		}
		cin >> s;
		BFS(s);
 
		for (int i = 1; i <= V; i++)
		{
			if (s != i)
			{
				int res = dist[i];
				if (res > 0)
					cout << res * 6 << " ";
				else
					cout << res << " ";
			}
		}
		cout << endl;
		//Xoá toàn bộ đồ thị để làm tiếp truy vấn tiếp theo
		for (int i = 0; i < V; i++)
		{
			graph[i].clear();
		}
	}
 
	return 0;
}
class Distance:
	def __init__(self, root, distance_cnt):
		self.root = root 
		self.distance_cnt = distance_cnt  #(k+1) elements list for distance from 0..k

	def get_distance_from_root(self, root):
		return self.distance_cnt

	def __repr__(self):
		return ''.join(str(self.distance_cnt))


def add(m1, m2):
	result = []

	for i in range(len(m1)):
		m1[i] = m1[i] + m2[i]


	return m1


def find_distance(root, pair, k=2):
	visited[root] = True 
	children = graph[root]
	distance_cnt = [0 for _ in range(k+1)]
	distance_cnt[0] = 1 

	distance_from_root = Distance(root, distance_cnt) #contains how many elements at a distance from the root


	if len(children) == 1 and visited[children[0]]: #leaf node
		print('leaf node {} current pair {}'.format(root, pair))
		if root in pair:
			print('node {} is in pair'.format(root))
			return [0 for _ in range(k+1)] 

		temp_distance = [0 for _ in range(k+1)]
		temp_distance[0] = 1

		return temp_distance #there is at least 1 node with distance 0 from the leaf node


	for child in children:
		if not visited[child]:
			
			temp_distance_ls = list(find_distance(child, pair, k))
			
			temp_distance_ls.insert(0, 0)
			temp_distance_ls.pop()
			add(distance_from_root.distance_cnt, temp_distance_ls)
			print('Dist root: ', distance_from_root.distance_cnt	

	return distance_from_root.distance_cnt



if __name__ == '__main__':
	n, k = map(int, input().split())
	graph = [[] for i in range(n)]
	visited = [False for i in range(n)]
	path = [-1 for i in range(n)]
	for i in range(n-1):
		u, v = map(int, input().split())
		graph[u-1].append(v-1)
		graph[v-1].append(u-1)

	result = []


	current_distance = 0
	distance_cnt = [0 for _ in range(k+1)]
	pair = set()

	for v in range(n):
		print('Visiting node: ', v)
		visited = [False for i in range(n)]
		result_distance_from_v = find_distance(v, pair, k)
		if result_distance_from_v[k] != 0:
			pair.add(v)
		print('Distance from root: {} is {}'.format(v, result_distance_from_v))

	print('Done')

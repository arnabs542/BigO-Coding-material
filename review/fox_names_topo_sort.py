

#assume name1 < name2 lexicographically
def processing_names(graph, name1, name2):
	name_len = min(len(name1), len(name2))
	flag = False

	for i in range(name_len):
		if name1[i] != name2[i]:
			graph[ord(name1[i]) - 97].append(name2[i])
			flag = True
			break

	if len(name1) > len(name2) and not flag:
		print('Impossible')
		exit(0)


def dfs_cycle(src):
	state[src] = 2

	for u in graph[src]:
		if state[ord(u)-97] == 2:
			print('Impossible')
			exit(0)

		if state[ord(u)-97] == 0:
			dfs_cycle(ord(u)-97)

	state[src] = 1
	result.append(src)



def topological_sort_dfs_cycle(graph, result):
	for i in range(26):
		if state[i] == 0:
			dfs_cycle(i)


	result.reverse()



if __name__ == '__main__':
	n = int(input())
	name_ls = []
	graph = [[] for i in range(26)]
	result = []
	state = [0] * 26
	for i in range(n):
		name_ls.append(input())

	#process the name list to figure out the alphabetical order
	for i in range(n-1):
		processing_names(graph, name_ls[i], name_ls[i+1])

	# for index, u in enumerate(graph):
	# 	print(index, u)

	topological_sort_dfs_cycle(graph, result)
	for element in result:
		print(chr(element + 97), end='')

	print()

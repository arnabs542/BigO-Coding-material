


# xxx  0 1 2
# xxx  3 4 5
# xxx  6 7 8

# octave = [x,x,x,x,x,x,x,x]

# n^2 * 7 * 7 * 7 ... * 7 ~ n^2 * 7^7
def check_valid(maze, row, col):
	if (row < 0 or row >= n or col >= n or col < 0 or maze[row][col] == '.'):
		#print('invalid col {} row {}'.format(col, row))
		return False

	return True


def back_track(maze, visited, octave, octave_ls, col, row):
	#print('Interim octave: ', octave)
	#print(visited)
  if len(octave) == 8:
    #if tuple(sorted(octave)) not in octave_ls:
    #print(octave)
    octave_ls.add(tuple(sorted(octave)))
    return

  if check_valid(maze, row, col) and not visited[row][col]:
    visited[row][col] = True
    octave.append(col + n*row)
    for i in range(4):
      col = col + dx[i]
      row = row + dy[i]

      #print('goto: i {} col {} row {}'.format(i, col, row))
      back_track(maze, visited, octave, octave_ls, col, row)
      col = col - dx[i]
      row = row - dy[i]

    visited[row][col] = False
    octave.pop()


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
if __name__ == '__main__':
  testcase = int(input())
  for case in range(testcase):
    n = int(input())
    maze = [[] for i in range(n)]
    octave = []
    octave_ls = set()

    for j in range(n):
      maze[j] = list(input())


    visited = [[False for i in range(n)] for j in range(n)]
    for col in range(n):
      for row in range(n):
        back_track(maze, visited, octave, octave_ls, col, row)

    print(len(octave_ls))

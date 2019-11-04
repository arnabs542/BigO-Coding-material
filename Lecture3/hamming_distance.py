def check(num):
  if sum(num) == 2:
    return True

  return False



def generate_dataset(n, h, pos, result):
  if check(result):
    print(*result,sep='')
    return

  for i in range(pos, 4):
    result[i] = 0
    generate_dataset(n, h, i+1, result)
    result[i] = 1



if __name__ == '__main__':
  testcase = int(input())
  for case in range(testcase):
    empty = input()
    n, h = map(int, input().split())
    result = [1] * 4
    generate_dataset(n, h, 0, result)
    print()

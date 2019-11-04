if __name__ == '__main__':
  testcase = int(input())
  for case in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))

    output_dict = {}
    for i in range(1, n+1):
      try:
        output_dict[arr[i-1]] += i * (n - i + 1)
      except:
        output_dict[arr[i-1]] = i * (n - i + 1)

    temp_result = 0
    for k,v in output_dict.items():
      if v % 2 != 0:
        temp_result ^= k
    print(temp_result)
		

#Wine trading

#Example:
# 5
# 5 -4 1 -3 1
# 6
# -1000 -1000 -1000 1000 1000 1000
# 0

if __name__ == '__main__':
  while True:
    n = int(input())
    if n == 0:
      break
    arr = list(map(int, input().split()))
    buy_arr = [0 for _ in range(n)]
    sell_arr = [0 for _ in range(n)]
    for i in range(n):
      if arr[i] > 0:
        buy_arr[i] = arr[i]
      else:
        sell_arr[i] = arr[i]

    total_work = 0
    i = 0
    j = 0

    # print(buy_arr)
    # print(sell_arr)

    while i < n and j < n:

      if buy_arr[i] > 0:
        while sell_arr[j] == 0:
          j += 1


        quantity = min(buy_arr[i], abs(sell_arr[j])) #4

        buy_arr[i] = max(buy_arr[i] - quantity, 0) #update buy remaining

        sell_arr[j] = min(sell_arr[j] + quantity, 0) #update sell remaining


        total_work += abs(j - i)*abs(quantity)

        if buy_arr[i] == 0:
          i += 1
        if sell_arr[j] == 0:
          j += 1

      else:
        i += 1

    print(total_work)


# 5 -4 1 -3 1

# 1 -> 0 4: 1 0 1 -3 1

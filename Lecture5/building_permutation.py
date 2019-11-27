#Stupid solution
#Building permutation

#1 2 3 4 5 6 .. n

if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().split()))
  total_move = 0
  number_set = set()

  for i in range(1, n+1):
    number_set.add(i)


  arr.sort()

  for i in range(n):
    change = 0
    if 1 <= arr[i] <= n:
      new_num = arr[i]
      if new_num in number_set:
        number_set.remove(new_num)
      else:
        new_num = arr[i-1] + 1
        while new_num not in number_set:
          new_num += 1
          change += 1

    elif arr[i] > n:
      #change = arr[i] - n
      new_num = n
      if new_num in number_set:
        number_set.remove(new_num)
      else:
        new_num = arr[i-1] + 1
        while new_num not in number_set:
          new_num -= 1
          change += 1
        number_set.remove(new_num)

    elif arr[i] < 1:
      #change = 1 - arr[i]
      new_num = 1

      if new_num in number_set:
        number_set.remove(new_num)
      else:
        new_num = arr[i-1] + 1
        while new_num not in number_set:
          new_num += 1
          change += 1
        number_set.remove(new_num)

    change = abs(new_num - arr[i])
    arr[i] = new_num
    #print(arr[i], new_num, change)
    total_move += change




  print(total_move)


 #Smarter solution
 #Building permutation

#1 2 3 4 5 6 .. n

if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().split()))
  total_move = 0
  number_set = set()

  for i in range(1, n+1):
    number_set.add(i)

  #target permutation
  #1 2 3 ... n
  target_permutation = [i+1 for i in range(n)]
  arr.sort()
  total_move = 0

  for i in range(n):
    total_move += abs(arr[i] - target_permutation[i])

  print(total_move)

  

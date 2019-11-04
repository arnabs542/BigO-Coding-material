



# Your last Python3 code is saved below:
# // print("Hello")



# // # Your last C/C++ code is saved below:
# // # # LOTTO
# // # # 1 2 3 5 8 13 21 34  --> k = 8

# // # # 5 + 1
# // # # 4 + 2
# // # # 3 + 3
# // # # 2 + 4
# // # # 1 + 5

# // # # 1 2 3 5 8 13  --> fix 8: 1 2 3 5 8
# // # # 1 2 3 5 8 21
# // # # 1 2 3 5 8 34
# // # # 1 2 3 5 13 8 (X)
# // # # 1 2 3 5 13 21 --> fix 5: 1 2 3 5
# // # # 1 2 3 5 13 34
# // # # 1 2 3 5 21 34
# // # # 1 2 3 8 13 21


# // # # 1 2 3 5 8 13 <-> 0 1 2 3 4 5
# // # # 1 2 3 5 13 21 <-> 0 1 2 3 5 6
# // # def processing(arr, temp, pos, end):
# // #   remaining_elements = arr[:]
# // #   print('remaining:', remaining_elements)
# // #   if pos == 5:
# // #     for final_val in remaining_elements:
# // #       temp[pos] = final_val
# // #       print(temp)

# // #   else:
# // #      # 1 2 3 5 8 13 21 34
# // #     temp[pos] = arr[pos]
# // #     processing(arr, temp, pos + 1, end)





# // # if __name__ == '__main__':
# // #   while True:
# // #     ls = list(map(int, input().split()))
# // #     k = ls[0]
# // #     if k == 0:
# // #       break
# // #     temp = [0] * 6

# // #     start = 0
# // #     end = 5
# // #     for i in range(start, end):
# // #       processing(ls[1:], temp, i, end)

# // #     print()

# //German lotto
# // arr: [1,2,3,4,5,6,7]
# 1 2 3 4 5 6  7 not used
# 1 2 3 4 5 7
# 1 2 3 4 6 7
# 1 2 3 5 6 7
# 1 2 4 5 6 7
# 1 3 4 5 6 7
# 2 3 4 5 6 7
#     1 2 3 4 5 6 7
#used T T T T T T F

#       [,,,,,]
#    |           |
#    v           v
# [1,,,,,]   [2,,,,,] ...
#    |
#    v
# [1,2,,,,]


#           [1,2,3,4,5,]
#       |                   |
#       v                   v
# [1,2,3,4,5,6]      [1,2,3,4,5,7]

# [3,,,,,] -> [3,4,,,,] -> ... -> [3,4,5,6,7, ]

def check(ins):
  if len(ins) == 6:
    return True

  return False



def generate(result, arr, pos):
  if check(result):
    print(*result)
    return

  for i in range(pos, k):
    #print('Interim result: ', result)
    result.append(arr[i])
    generate(result, arr, i + 1)
    result.pop()






if __name__ == '__main__':
    while True:
        ins = list(map(int, input().split()))
        if ins[0] == 0:
            break

        k = ins[0]
        res = []
        result = generate(res, ins[1:], 0)
        #print(result)


##Power of Two 
#
#|S| = n
#
#010101..0101 (n bits)
#
#S = [1, 2, 3]
#
#[1] -> 100
#[2, 3] -> 011
#
#2^n subsets <-> 2^n strings
#
#000 = []
#001 = [3]
#010 = [2]
#011 = ..
#...
#111 = [1, 2, 3]


#Power of Two 





if __name__ == '__main__':
  testcase = int(input())
  
  
  #print(power_two_ls)
  
  for case in range(testcase):
    flag = False
    n = int(input())
    ls = list(map(int, input().split()))
    for k in range(32):
      one_index = k
      possible_subset = []
      for num in ls:
        if (num >> k) & 1:
          possible_subset.append(num)

      
      #print(possible_subset) 
      if len(possible_subset) > 0:
        result = possible_subset[0]
        for i in range(1, len(possible_subset)): # number of 1 is smallest when AND all elements 
        
          result = result & possible_subset[i] 
         
        if result & (result-1) == 0: #power of two or can check the digit at Kth position
          flag = True
          
          break
    
    if flag: 
      print('YES')
    else:
      print('NO')

#Roma and Changing Signs


n, k = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
current_sum = 0 

while True:
  if k <= 0:
    break
    
  if arr[i] < 0:
    arr[i] *= (-1) #convert to positive
    k -= 1 #perform one conversion
    
    
  
  elif arr[i] > 0:
    arr[i] *= (-1)
    k -= 1
    if (k > 0) and (arr[i] < 0):
      k -= 1 #perform two conversions
      arr[i] *= (-1)
    
  else: #if arr[i] == 0 --> start of positive section
    break
  
  current_sum += arr[i]
  
  if i < n-1 and current_sum + arr[i+1] < current_sum:
    i += 1 #increase to next number


print(sum(arr))
     
    


# 4 4
# -100 -90 -1 -1
#100 90 1 -1

# 4 4
# -100 -90 -5 2

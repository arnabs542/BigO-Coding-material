k = int(input())
n = int(input())

# k = 11
# 81 -> 89 
# 91 -> 99 (2 steps)

digits_in_n = sorted(list(int(i) for i in str(n)))
#print(digits_in_n)

i = 0
count = 0
current_sum = sum(digits_in_n)
while current_sum < k:
  if digits_in_n[i] < 9:
    current_sum = current_sum - digits_in_n[i] + 9
    digits_in_n[i] = 9
    count += 1
  i += 1

print(count)

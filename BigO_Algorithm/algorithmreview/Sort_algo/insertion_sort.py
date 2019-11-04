#Insertion sort
def insertion_sort_a(array_value):
    for i in range(len(array_value)):
        j = i
        while ((j > 0) and (array_value[j] < array_value[j-1])):
            array_value[j], array_value[j-1] = array_value[j-1], array_value[j]
            j -= 1
            print(array_value)
array_a = [9,1,10,2,4,5,6,7,3,5,4,0,2,8]
print('Input: ', end = '')
print(array_a)
print()
insertion_sort_a(array_a)
print(array_a)

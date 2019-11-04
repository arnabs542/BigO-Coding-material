import copy



def minimize_absolute_difference(ins, value_arr, index_arr, pos):
  global min_value
  global index_result
  global val_result

  #print(value_arr)
  if pos == 4:

    if val_result[0] == None:
      val_result = copy.copy(value_arr)
      index_result = copy.copy(index_arr)

    else:
      new_numerator = abs(value_arr[0]*value_arr[3] - value_arr[1]*value_arr[2])
      new_denominator = value_arr[1] * value_arr[3]

      old_numerator = abs(val_result[0] * val_result[3] - val_result[1]*val_result[2])
      old_denominator = val_result[1] * val_result[3]

      if new_numerator * old_denominator < old_numerator * new_denominator:

        index_result = copy.copy(index_arr)
        val_result = copy.copy(value_arr)



      elif new_numerator * old_denominator < old_numerator * new_denominator:

        if index_arr < result:
          index_result = copy.copy(index_arr)


    return

  for i in range(len(ins)):
    if i not in index_arr:
      value_arr[pos] = ins[i]
      index_arr[pos] = i
      minimize_absolute_difference(ins, value_arr, index_arr, pos+1)
      value_arr[pos] = None
      index_arr[pos] = None


if __name__ == '__main__':
  ins = list(map(int, input().split()))
  value_arr = [None] * 4
  index_arr = [None] * 4
  val_result = [None, None, None, None]
  index_result = [None, None, None, None]
  min_value = 100000000
  minimize_absolute_difference(ins, value_arr, index_arr, 0)
  print(*index_result)

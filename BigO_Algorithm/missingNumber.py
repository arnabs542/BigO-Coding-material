def findMissing(a):
    cnt = [0 for i in range(len(a)+2)]
    for i in range(len(a)):
        if cnt[a[i]] == 0:
            cnt[a[i]] = 1
        else:
            cnt[a[i]] += 1
    result = []
    A = -1
    B = -1
    for i in range(1,len(a)+1,1):
        if cnt[i] == 2:
            A = i
        if cnt[i] == 0:
            B = i
    result.append(A)
    result.append(B)
    return result

if __name__ == '__main__':
    input_array = (3, 1, 2, 5, 3)
    print(findMissing(input_array))
    

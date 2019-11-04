#German lotto
def generate(k, arr):
    result = [0] * 6
    for i in range(k):
        result[i] = arr[i]



if __name__ == '__main__':
    while True:
        ins = list(map(int, input().split()))
        if ins == 0:
            break
        k = ins[0]
        result = generate(k, ins)
        for res in result:
            print(res)

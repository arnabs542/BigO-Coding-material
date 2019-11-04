#Street Parade
#Staff solution
while(True):
    n = int(input())
    if (n == 0):
        exit()
    street = 1
    flag = 0
    track = [1001]
    for car in map(int, input().split()):
        if (car != 0):
            if car == street:
                street += 1
            else:
                while(street == track[-1]):
                    street += 1
                    track.pop()
                if (car > track[-1]):
                    flag = 1
                else:
                    track.append(car)
        print(car, street)
        print(track)

    if (flag == 0):
        print("yes")
    else:
        print("no")

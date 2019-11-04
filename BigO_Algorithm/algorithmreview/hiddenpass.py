#Hidden password
testcase = int(input())
x_left = 0
y_left = 0
x_right = 0
y_right = 0
for case in range(testcase):
    num_obj = int(input())
    for i in range(num_obj):
        ls = list(input().split())
        if ls[0] == 'c':
            tmp_x_left = int(ls[1]) - int(ls[3])
            tmp_y_left = int(ls[2]) - int(ls[3])
            tmp_x_right = int(ls[1]) + int(ls[3])
            tmp_y_right = int(ls[2]) + int(ls[3])
        elif ls[0] == 'p':
            tmp_x_left = int(ls[1])
            tmp_y_left = int(ls[2])
            tmp_x_right = int(ls[1])
            tmp_y_right = int(ls[2])
        elif ls[0] == 'l':
            tmp_x_left = int(ls[1])
            tmp_y_left = int(ls[2])
            tmp_x_right = int(ls[3])
            tmp_y_right = int(ls[4])
        if i == 0:
            x_left = tmp_x_left
            y_left = tmp_y_left
            x_right = tmp_x_right
            y_right = tmp_y_right
        else:
            if x_left > tmp_x_left:
                x_left = tmp_x_left
            if y_left > tmp_y_left:
                y_left = tmp_y_left
            if x_right < tmp_x_right:
                x_right = tmp_x_right
            if y_right < tmp_y_right:
                y_right = tmp_y_right
    print(x_left, y_left, x_right, y_right, end = ' ')
    print('\n')




#Googol
def reverse(str_input):
    new_str = []
    for i in range(len(str_input)-1,-1,-1):
        new_str.append(str_input[i])
    return ''.join(new_str)

def switch(str_input):
    new_str = []
    for i in range(len(str_input)):
        if str_input[i] == '0':
            new_str.append('1')
        else:
            new_str.append('0')
    return ''.join(new_str)

def googol(degree):
    if degree == 1:
        return '0'
    else:
        return googol(degree - 1) + '0' + switch(reverse(googol(degree-1)))


if __name__ == '__main__':
    print(googol(100000))
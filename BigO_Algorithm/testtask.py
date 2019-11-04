#Test Task
n = int(input())
d = dict()
login_lst = []
for i in range(n):
    lst = list(input().split())
    if lst[0] == 'register':
        if lst[1] not in d:
            d[lst[1]] = lst[2]
            print('success: new user added')
        else:
            print('fail: user already exists')
    elif lst[0] == 'login':
        if lst[1] not in d:
            print('fail: no such user')
        else:
            if lst[1] in login_lst:
                print('fail: already logged in')
            else:
                if lst[2] != d[lst[1]]:
                    print('fail: incorrect password')
                else:
                    login_lst.append(lst[1])
                    print('success: user logged in')
    elif lst[0] == 'logout':
        if lst[1] not in d:
            print('fail: no such user')
        else:
            if lst[1] not in login_lst:
                print('fail: already logged out')
            else:
                login_lst.remove(lst[1])
                print('success: user logged out')
    
                    
            
        

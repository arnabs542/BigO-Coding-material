#Throwing cards
import queue
while True:
    n = int(input())
    if n == 0:
        break
    q = queue.Queue()
    for i in range(n):
        q.put(i+1)

    st = []
    while q.qsize() > 1:
        st.append(q.get())
        tmp = q.get()
        q.put(tmp)

    print('Discarded cards:', str(st)[1:-1])
    print('Remaining card:', q.get())
        

    
    

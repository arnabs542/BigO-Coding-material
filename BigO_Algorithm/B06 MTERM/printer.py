#Printer priority
import queue

if __name__ == '__main__':
    testcase = int(input())
    for cs in range(testcase):
        
        n, m = map(int,input().split())
        my_pos = m

        q = queue.Queue()
        pq = queue.PriorityQueue()

        lst = list(map(int,input().split()))
        my_priority = lst[m]
        max_value = lst[0]
        for item in lst:
            q.put(item)
            pq.put(-item)
        count = 0
        flag = True

        while flag:
            #print(q.queue)
            #print(pq.queue)
            tmp = q.get()
            if tmp < abs(pq.queue[0]):
                q.put(tmp)
                if my_pos > 0:
                    my_pos = my_pos - 1
                else:
                    my_pos = q.qsize() - 1
            elif tmp == abs(pq.queue[0]):
                pq.get()
                count += 1
                if my_pos == 0:
                    flag = False
                else:
                    my_pos = my_pos - 1

        print(count)
    
        
        
    

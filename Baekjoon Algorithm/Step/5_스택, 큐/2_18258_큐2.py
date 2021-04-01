import sys
from collections import deque
#큐는 deque를 사용하는 것이 더 빠르다.

num = int(input())
list_num = deque([])

for i in range(num):
    a = sys.stdin.readline().split()
    try:
        if(a[0] == "push"):
            list_num.append(int(a[1]))
        elif(a[0] == "pop"):
                print(list_num.popleft())
        elif(a[0] == "size"):
            print(len(list_num))
        elif(a[0] == "empty"):
            if(len(list_num) == 0):
                print(1)
            else:
                print(0)
        elif(a[0] == "front"):
            print(list_num[0])
        elif(a[0] == "back"):
            print(list_num[-1])
    except IndexError:
        print(-1) 
    

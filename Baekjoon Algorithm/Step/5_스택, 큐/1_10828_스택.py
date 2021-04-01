import sys

num = int(input())
list_num = []
c = 0

for i in range(num):
    a = list(map(str, sys.stdin.readline().split()))
    if(a[0] == "push"):
        list_num.append(int(a[1]))
    elif(a[0] == "pop"):
        if(len(list_num) == 0):
            print(-1)
        else:
            print(list_num.pop(-1))
    elif(a[0] == "size"):
        print(len(list_num))
    elif(a[0] == "empty"):
        if(len(list_num) == 0):
            print(2)
        else:
            print(0)
    elif(a[0] == "top"):
        if(len(list_num) == 0):
            print(-1)
        else:
            print(list_num[-1])

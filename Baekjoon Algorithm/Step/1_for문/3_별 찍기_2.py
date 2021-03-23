a = int(input())

for i in range(1, a+1):
    for k in range(1, a-i+1):
        print(" ", end='')
    for j in range(0, i):
        print("*", end='')
    print()
import sys

a = int(input())

for i in range(1, a+1):
    b, c = map(int, sys.stdin.readline().split())
    s = 'Case #{0}: {1} + {2} = {3}'.format(i,b,c,b+c)
    print(s)
    
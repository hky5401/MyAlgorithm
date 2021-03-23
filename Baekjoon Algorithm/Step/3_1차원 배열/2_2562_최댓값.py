a = []

for i in range(9):
    num = int(input())
    a.append(num)

b = max(a)
print(b)
print(a.index(b)+1)

## index 0을 포함해서 개수를 세기 떄문에 +1을 해준다.
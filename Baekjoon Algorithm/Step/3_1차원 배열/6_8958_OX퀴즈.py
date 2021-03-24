num = int(input())
count = 0
re = 0
list_plus = []

for i in range(num):
    s = input()
    for j in range(len(s)):
        if s[j] == 'O':
            count += 1
            re += count
        elif s[j] == 'X':
            count = 0
    list_plus.append(re)
    count = 0
    re = 0

for i in range(len(list_plus)):
    print(list_plus[i])
a = int(input())
b = int(input())
c = int(input())

num = a * b * c
s = str(num)

num_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(s)):

    if s[i] == '0':
        num_list[0] += 1
    elif s[i] == '1':
        num_list[1] += 1
    elif s[i] == '2':
        num_list[2] += 1
    elif s[i] == '3':
        num_list[3] += 1
    elif s[i] == '4':
        num_list[4] += 1
    elif s[i] == '5':
        num_list[5] += 1
    elif s[i] == '6':
        num_list[6] += 1
    elif s[i] == '7':
        num_list[7] += 1
    elif s[i] == '8':
        num_list[8] += 1
    elif s[i] == '9':
        num_list[9] += 1


for i in range(10):
    print(num_list[i])


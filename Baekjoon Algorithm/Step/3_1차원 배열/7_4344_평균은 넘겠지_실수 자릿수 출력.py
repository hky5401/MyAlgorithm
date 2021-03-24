num = int(input())
result = []

for i in range(num):
    num_list = list(map(int, input().split()))
    people = len(num_list) - 1
    avg = sum(num_list)-num_list[0]
    avg /= people
    count = 0
    for j in range(1, len(num_list)):
        if(num_list[j] > avg):
            count += 1
    re = count / people
    re *= 100
    result.append(re)

for i in range(len(result)):
    print('%.3f' % result[i],end='')
    print('%')
num_list = []

for i in range(10):
    num = int(input()) % 42
    if num_list.count(num) == 0:
        num_list.append(num)


print(len(num_list))
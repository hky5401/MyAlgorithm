def d(num):
    for i in str(num):
        num += int(i)

    return num    

a = {}
a = set()

for i in range(1, 10001):
    num = i
    while(True):
      num = d(num)
      if num > 10000: break
      a.add(num)
      

num_list = list(a)
num_list.sort()
count = 0

for i in range(1, 10001):
    if (i == num_list[count]):
        count += 1
    else:
        print(i)
    
num = int(input())
count = 0

if(num<10):
    num = num * 10
    
result = num

while(True):
    count = count + 1

    a = num % 10
    b = int(num/10)

    num = (a + b) % 10
    num = (a*10) + num

    if(result == num): break
    
print(count)

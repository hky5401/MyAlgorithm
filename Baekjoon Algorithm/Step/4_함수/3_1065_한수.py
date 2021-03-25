def d(num):
    s = str(num)
    num = int(s[1]) - int(s[0]) 
    for i in range(2, len(s)):
        m = int(s[i-1]) + num
        if(m != int(s[i] or num==0)):
            return 0
    
    return 1


num = int(input())
count = 0

for i in range(1, num+1):
    if(i < 100):
        count += 1
    else:
        count += d(i)
        
print(count)
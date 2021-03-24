num = int(input())

subject = list(map(int, input().split()))
max_sub  = max(subject)
avg_sub = 0

for i in range(len(subject)):
    subject[i] = subject[i] / max_sub * 100
    avg_sub += subject[i]

print(avg_sub / len(subject))
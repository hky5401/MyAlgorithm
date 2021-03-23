import sys
# list map을 넣으면 list값을 하나씩 받고 싶은 만큼 받을 수 있다.
a, b = map(int, input().split())
A = list(map(int, input().split()))

for i in range(a):
    if(A[i] < b): print(A[i], end=' ')

#map 함수
#map(f, iterable)
# 함수(f)와 반복 가능한 자료형(iterable) 입력으로 받는다.
# 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
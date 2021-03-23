while(True):
   try:
        a, b = map(int, input().split())
        print(a+b)
   except:
        break


# try except으로 예외를 발생시켜 입력값이 잘못되거나 초과되면 break 처리해준다. 
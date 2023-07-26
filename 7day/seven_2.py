
di = {}
i = 0
while True:
    inputvalue = input('키 이름을 입력하시오')
    i = i + 1
    if inputvalue == 'q':
        exit()
    di.setdefault(i, inputvalue)
    print(di)

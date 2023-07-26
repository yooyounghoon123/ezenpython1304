a = 1


def vartest():
    # global a
    b = 0  # 초기값을 설정하지 않으면 오류가 난다
    result = b + 1
    global a
    a = result
    print(a)


vartest()

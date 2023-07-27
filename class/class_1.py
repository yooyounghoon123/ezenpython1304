result=0

def add(num):
    #glbal 전역변수 쓰겠다
    global result
    #result=result + num
    result+=num
    # return result
    print(result)


(add(1))
(add(2))
print(result)

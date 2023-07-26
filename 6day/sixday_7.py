def home(**args):
    print(args)


home(name='유영훈', age=25, address='종암동')


# 1,2,3,4,5 -> 일반변수 메소드
# 일반변수 1,2    *3,4,5 -> 일반변소 메소드
# 일반변수1,2,3  **기4:4, 키5:5 -> 일반변소 메소드



def a(number1,number2,number3,number4,number5):
    for i in range(1,6):
        result=result+i
    print(result)

def b(number1,number2,*number3):
    for i in range(1,6):
        




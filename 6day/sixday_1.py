name = '유영훈'
age = 25
address = '종암동'

# 변수는 한타입만 받을수 있다
# 저장할 수 있다

print('안녕하세요')


# 함수(method) -> 괄호안에 갯수에 상관없고 어떤 타입이든 담을수있다
# python method 선언 def 매소드이름(): <- 함수(method)
# 함수 (method) -> call한다 호출한다 자기자신이 호출 할 수 없다
def name():
    print('유영훈')

def age():
    print(25)

def adress():
    print('종암동')


# name() call 한다
name()
age()
adress()

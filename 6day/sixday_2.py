name = '유영훈'

# f=string f' {변수}' 변수명 대입
# 지역변수: 해당하는 문이 끝나면 (괄호) 소명한다


# def name(name):
#     print(f'이름은 {name} 입니다')

# i=0
# for i in range(1,11):
#     result = 0
#     # print(i)
#     result = result + i
#
# print(result) # 전역변수


# 매개변수 인자 아퀴먼트 지역변수
def printsve(name):
    print(f'{name} 입니다')


def age(age):
    print(f'나이는 {age} 입니다')


def address(address):
    print(f'사는 지역은 {address} 입니다')


printsve('유영훈')
age(25)
address('종암동')


def home(name, age, address):
    print(f'이름은 {name} 나이는 {age} 사는 지역은 {address} 입니다')


home('유영훈', 25, '종암동')

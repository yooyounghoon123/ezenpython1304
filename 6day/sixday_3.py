# static 변수 지역변수
name = '유영훈'
age = 25
address = '종암동'


def name():
    # 지역변수
    name = '유영훈'
    return name


def age():
    age=25
    return age


def address():
    address='런던'
    return address

print(name())
print(age())
print(address())


# 이름,나이,주소 아규먼트(인자, 매소드) 받고 리턴해서 출력



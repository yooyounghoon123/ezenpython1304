# 메소드는 오버로딩이 안된다 -> 메소드 이름을 다른 메소드 명으로 들수 없다
# 오버로딩: 메소드 이름

def name(*home):
    print(home)


def home2(*name):
    return name


def home3(name, *home):
    print(f'이름은 {name} 나머지는 {home} 입니다')


name('유영훈', 25, '종암동')
print(home2('김현종', 25, '종암동'))
home3('유영훈', 25, '종암동')

print('='*50)

# (이름 나이 주소) 일반 변수 + 이메일 폰번호
def home4(name, age, address, *etc):
    print(f'이름은 {name} 나이는 {age} 주소는 {address} 이메일과 핸드폰번호는 {etc}')

home4('유영훈', 25, '종암동', 'rjhj1181@naver.com', '01038862891')







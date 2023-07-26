
#[] <- 인덱스 기호 안에서 문자열은 처음에 0부터 시작.
#슬라이싱 :의 오른쪽은 미만.

number = '123 456 789'
#[0:]일 때 문자열 0번에서부터 끝까지 인덱싱 한 것.
print(number[0:])
print(number[4:])

home = '김채성 24 김포시 아무개동'

print(len(home))
print('길이는:',home[0:3],'나이는:',home[4:6],'주소는:',home[-4:])
print('나이는:',home[4:6])
print('주소는:',home[-4:])


number='123 456 789'
print(number)
print(len(number))

#모든 언어는 문자열의 공백도 길이로 본다.
#문자열에서 문자의 번호는 처음에 0번부터 시작.

number='123456789'
print(number[0])

#본인 이름 3번째 문자 출력, 주소에서 '시' 앞까지 출력


name='김채성'
address='경기도 김포시'
print(name[2])
print(address[4]+address[5]) #  <-- 일종의 문자열 연산을 한 건가? 문자 연산?

number='123456789'
print(number[6])
print(number[-3])

#1 3 6 index 출력
# 역 index 출력

print(number[0]+number[2]+number[5])
print(number[-0]+number[-7]+number[-4])
print((number[0]+number[2]+number[5])*2)





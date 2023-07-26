printname='이름은 김채성 입니다'
print(printname)

#ctrl+shift+f10 빠른 실행 , ctrl+f5 디버그

printname="이름은 김현호's 입니다"
print(printname)

printname="이름은 김현호\'s 입니다"
print(printname)

print('안녕하세요 반가워요')


#이름,나이,주소를 변수 선언 없이 값으로만 출력해라.

print('김채성')
print('24')
print('경기도 김포시')

#Q. 이 때 출력된 값의 자료형은 문자열인 건가??

#이름,나이,주소를 변수 선언하고 출력해라.

name='김채성'
age=24
adress='경기도 김포시'
print(name)
print(age)
print(adress)

#본인 나이에 5를 더하고 출력하시오.

print(age+5)

#end : 줄 바꿈 일어나지 않게 한다.
#\n : 줄 바꿈.

print("줄 바꿈이 일어나지 않는다",end="")
print("다음 글이다.")
print('12345\n6789')
print(77)

multiline = '''
줄 바꿈 테스트 
줄 바꿈 테스트
이렇게 입력하면 보기 편하다.
'''
print(multiline)

#tab
print('12345\t6789')
#\ 어떠한 기호를 출력하고 싶을 때.
print('12345\\6789')





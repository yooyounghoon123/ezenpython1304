class Ezen14:

    def printe(self):
        print('=' * 50)

    def __init__(self, roomnumber,roomcheck):
        #self.roomnumber 전역변수
        #python 초기값을 넣어야한다 아니면 에러
        #지역변수는 해당하는 문이 닫히면 소멸한다
        #지역변수가 소멸되기전에 전역변수에 담는다
        self.roomnumber = roomnumber
        self.roomcheck = roomcheck

    def printe(self):
        print(f'{self.roomnumber}호')
        print(f'{self.roomcheck}명')




ezen14 = Ezen14('1401호', 6)

#object -> 모든 타입을 담을수 있다

ezen14.
ezen15 = Ezen14('1402호', a, c)
ezen16 = Ezen14('1403호', a, c)

ezen14.ezen13print()
ezen14.printe()

ezen15.ezen13print()
ezen14.printe()

ezen16.ezen13print()
ezen14.printe()

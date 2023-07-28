while True:

    class Room1304:

        a = input('현재 인원을 입력하세요')
        b = input('추가 인원을 입력하세요')
        c = input('빠진 인원을 입력하세요')

        def setdata(self, a, b, c, result):
            self.a = a
            self.b = b
            self.c = c
            self.result = result

        def now(self):
            self.a = self.a
            print(f'현재 인원은 ', self.a)

        def add(self):
            self.b = self.b
            print(f'추가 인원은 ', self.b)

        def sub(self):
            self.c = self.c
            print(f'빠진 인원은 ', self.c)

        def total(self):
            self.result = int(self.a) + int(self.b) - int(self.c)
            print(f'총 인원은 ', self.result)


    r1304 = Room1304()
    r1304.now()
    r1304.add()
    r1304.sub()
    r1304.total()

    r1304=Room1304()
    r1305=Room1304()
    choice=[r1304,r1305]

    if input() == 'q':
        exit()

class Room1304:

    def __init__(self):
        self.i = 0
        self.a = 0
        self.b = 0
        self.result = 0

    def now(self, num):
        self.i = self.i + num
        print(f'현재인원은 ', self.i)

    def add(self, num):
        self.a = self.a + num
        print(f'추가인원은 ', self.a)

    def sub(self, num):
        self.b = self.b - num
        print(f'빠진인원은 ', -self.b)

    def total(self):
        self.result = self.i + self.a + self.b
        print(f'남은 총 인원은 ', self.result)


r1304 = Room1304()
r1304.now(5)   # 현재 인원 입력
r1304.add(2)   # 추가 인원 입력
r1304.sub(1)   # 탈주한 인원 입력
r1304.total()  # 남은 총 인원 수

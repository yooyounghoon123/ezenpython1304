class Calv:

    # 객체(isinstance) 생성할때 초기값
    # 메모리 상주
    # self 해당하는 객체을 넘기겠다 여기서는 Calv 타입
    def __init__(self):
        self.result = 0
        self.result2 = 0

    def add(self, num):
        self.result = self.result + num
        return self.result

    def add2(self, num):
        self.result2 = self.result2 + num
        return self.result2

    # 큰데에서 작은데로
    # 대한민국.서울.강남구.서초4동.w.13층.1304

# Calv() 객체생성
caluob=Calv()

caluob.add(1)
caluob.add(2)
caluob.add(3)
print(caluob.add(4))

for i in range(1,6):
    print(caluob.add2(i))

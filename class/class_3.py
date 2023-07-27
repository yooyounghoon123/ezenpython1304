class Calu2:

    def __init__(self):
        self.result=0
        self.result2=0
        #self는 전역변수가 된다

    def add(self,num):
        self.result=self.result+num

    def add2(self,num):
        self.result2=self.result2-num

    def printtotal(self):
        print(self.result)

    def printtotal2(self):
        print(self.result2)


cal=Calu2()
cal.add(10)
cal.add(20)
cal.printtotal()

cal.add2(10)
cal.add2(20)
cal.printtotal2()

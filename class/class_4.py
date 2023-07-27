class Fourcal:

    def setdata(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        result= self.a + self.b
        return result

fcal=Fourcal()
fcal.setdata(1,2)
print(fcal.add())



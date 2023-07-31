from etc.parent import parent_1

class namemethod_1(parent_1):

  def __init__(self,name,age,address):
    self.name=name
    self.age=age
    self.address=address
    super.__init__(self,name,age,address)



    def namemethod(self):
        print(self.name)


ob=namemethod_1('이름',10,'미국')
ob.namemethod()
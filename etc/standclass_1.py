# from package import class
from etc.abstractclass_1 import abstractclass_1


class standclass_1(abstractclass_1):

    def __init__(self,ob):
        self.ob=ob
    def abstract_method(self, input):
        print(self.ob)
        print(input)


sc = standclass_1('타입')
sc.abstract_method('입력')

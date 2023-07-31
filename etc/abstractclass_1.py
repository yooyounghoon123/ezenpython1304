# 추상클래스: 추상클래스는 추상매소드가 오면 객체생성을 할수없다
# 추상매소드가 없으면 객체생성을 할수있다
# 추상클래스는 반드시 ABCMETA을 상속 받아야한다


# from abc-> 패키지이름  abc.ABCMeta abc,abstractmethod
from abc import ABCMeta, abstractmethod


# (metaclass=ABCMeta) -> 추상클래스 선언 (abstract class)
class abstractclass_1(metaclass=ABCMeta):

    def __init__(self, ob):
        self.ob = ob

    def standmethod(self,input):
        print(self.ob)
        print(input)

    #추상매소드는 몸체가 없다
    #추상매소드를 상속받는 클래스는 반드시 몸체구현을 해주어야한다 아니면 에러
    #자식은 객체생성을 할수있다 (일반클래스)

    @abstractmethod
    def abstract_method(self):
        pass


# ac = abstractclass_1('타입')
# ac.standmethod()

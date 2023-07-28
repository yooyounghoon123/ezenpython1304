from class2 import parent


class Icefactory(parent):

    def __init__(self, commanyname, icetype):
        self.commanyname = commanyname
        self.icetype = icetype
        print('init')

    # 오버라이딩->부모에있는 매소드 이름,타입,갯수가 같으면 자식이 부모에있는 매소드를 재정의한다
    # 오버로딩->매소드명은 같은데 리턴타입 아귀먼트 타입, 아귀먼트 갯수가 틀린경우
    def parentmethod(self):
        print('parentmethod')

class classmethod_1:

    def __init__(self, name):
        self.name = name

    def standmethod(self):
        print(self.name)

    # classmethod 해당하는 생성자를 호출해서 리턴한다
    @classmethod
    def class_method(cls):
        return cls('아무개')

    cm = classmethod_1('유영훈')
    cm.standmethod()
    cm2=cm.class_method()
    cm.standmethod()

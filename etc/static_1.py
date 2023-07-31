class static_1:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def standmethod(self, input):
        print(self.name)
        print(self.age)
        print(self.address)
        print(input)


    #staticmethod: self로는 접근하지 못한다
    @staticmethod
    def static_method(input):
        print('static method')
        print(input)


st = static_1('유영훈', 25, '종암동')
st.standmethod('입력')
st.static_method('입력')
static_1.static_method('입력2')
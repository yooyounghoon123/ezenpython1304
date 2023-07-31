class parent_1:

    def __int__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

        print(self.name)
        print(self.age)
        print(self.address)

    def home(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

        print(self.name)
        print(self.age)
        print(self.address)

pa=parent_1()
pa.home('유영훈',25,'종암동')




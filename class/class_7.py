class class5:

    def __init__(self,roomname,name,age):
        self.roomname=roomname
        self.name=name
        self.age=age

cl5=class5('room1304','유영훈',25)
print(cl5.roomname)
print(cl5.name)
print(cl5.age)

cl6=class5('room1305','아무개',25)
print(cl6.roomname)
print(cl6.name)
print(cl6.age)
a=[cl5,cl6]

print(type(cl5))
print(type(cl6))

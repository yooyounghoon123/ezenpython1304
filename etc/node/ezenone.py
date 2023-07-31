from etc.node.ezen_factory1 import ezen_factory1


class ezenone(ezen_factory1):

    def printezename(self):
        print('ezen one')


ez = ezenone('ezen', 'room1301', 'html', 6)
# print(ez.school_name())
# print(ez.room_number())
# print(ez.room_type())
# print(ez.person_count())

ez2 = ezenone('ezen', 'room1302', 'css', 7)

ez3 = ezenone('ezen', 'room1303', 'javascript', 3)

ez4 = ezenone('ezen', 'room1304', 'python', 5)

ezenlist = [ez, ez2, ez3, ez4]

for i in ezenlist:
    print(i.school_name())
    print(i.room_number())
    print(i.room_type())
    print(i.person_count())
    print('=' * 30)

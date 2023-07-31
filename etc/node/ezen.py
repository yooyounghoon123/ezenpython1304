from abc import ABCMeta, abstractmethod


class ezen(metaclass=ABCMeta):

    # schoolname: 학원이름-> 이젠, roomumber-> 호수, roomtype-> 과목, personcount-> 학생수

    def __init__(self, schoolname, roomnumber, roomtype, personcount):
        self.schoolname = schoolname
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.personcount = personcount

    def school_name(self):
        return self.schoolname

    def room_umber(self):
        return self.roomnumber

    def room_type(self):
        return self.roomtype

    def person_count(self):
        return self.personcount

    @abstractmethod
    def roommake(self,schoolname, roomnumber, roomtype, personcount):
        pass


# ez = ezen('ezen', 'room1304', 'python', 5)
# print(ez.school_name())
# print(ez.room_umber())
# print(ez.room_type())
# print(ez.person_count())

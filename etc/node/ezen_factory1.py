from etc.node.ezen import ezen

class ezen_factory1(ezen):

    def roommake(self,schoolname, roomnumber, roomtype, personcount):
        self.schoolname = schoolname
        self.roomnumber = roomnumber
        self.roomtype = roomtype
        self.personcount = personcount

    def school_name(self):
        return self.schoolname

    def room_number(self):
        return self.roomnumber

    def room_type(self):
        return self.roomtype

    def person_count(self):
        return self.personcount



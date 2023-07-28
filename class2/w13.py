class Ezen13:

    # 1301~1306
    #     1301 html 1302 jqery 1303 css 1304 python 1305 java 1306 ai

    # rnumber s 방번호 rtotal i 인원수 checkncs s uncs subject 과목

    def printe(self):
        print('='*50)

    def __init__(self, rnumber, rtotal, checkncs, subject):
        self.rnumber = rnumber
        self.rtotal = rtotal
        self.checkncs = checkncs
        self.subject = subject

    def ezen13print(self):
        print(self.rnumber)
        print(self.rtotal)
        print(self.checkncs)
        print(self.subject)


ezen13 = Ezen13('1301', 5, 'ncs', 'html')
ezen14 = Ezen13('1302', 5, 'ncs', 'jqery')
ezen15 = Ezen13('1303', 5, 'uncs', 'css')
ezen16 = Ezen13('1304', 5, 'ncs', 'python')
ezen17 = Ezen13('1305', 5, 'uncs', 'java')
ezen18 = Ezen13('1306', 5, 'ncs', 'ai')


ezen13.ezen13print()
ezen13.printe()

ezen14.ezen13print()
ezen13.printe()

ezen15.ezen13print()
ezen13.printe()

ezen16.ezen13print()
ezen13.printe()

ezen17.ezen13print()
ezen13.printe()

ezen18.ezen13print()
ezen13.printe()

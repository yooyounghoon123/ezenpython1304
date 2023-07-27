result = 0


def num(input):
    global result
    result = input
    return result


print(num('입력'))


class room1304:
    # self 현재 해당하는 객체(instance)
    def name(self):
        return 'self 객체'

    def prname(self,name):
        print(f'이름은 {name} 입니다')


#객체지향은 큰데에서 작은데로 간다
#지구.대한민국.서울.깅남구.w건물.13층.1304호
r1304 = room1304()
print(r1304.name())
r1304.prname('유영훈')

r1304_2=room1304()
r1304_2.prname('아무개')

# print(id(r1304))
# print(id(r1304_2))

print('='*50)

class python1304:
    def first(self):
        sum1=0
        for i in range(1,11):
            sum1=sum1+i
        return sum1

    def two(self):
        sum2=0
        for j in range(11,21):
            sum2=sum2+j
        print(f'11~20까지 합은 {sum2}')

p1304=python1304()
print('1~10까지 합은', p1304.first())

p1304_2=python1304()
p1304_2.two()

print('='*50)







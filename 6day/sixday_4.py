a = [1, 2, 3, 4]
b = []

for i in a:
    b.append(i * 2)

print(b)
print('=' * 50)

# 1~10까지 리스트를 만들고 a b 리스트에 홀수의 값만 저장
a = []
b = []

for i in range(1, 11):
    a.append(i)
    if i % 2 != 0:
        b.append(i)

print(b)
print('=' * 50)

# 1~5 a  b는 짝수만 저장  c는 홀수만 저장
a = []
b = []
c = []
d = []

# for i in range(1,6):
#     a.append(i)
#     if i % 2 == 0:
#         b.append(i)
#     else:
#         c.append(i)
# 
# print(a)
# print(b)
# print(c)

for i in range(1, 6):
    a.append(i)

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

one = 0
for i in b:
    one = one + i
d.append(one)

two = 0
for i in c:
    two = two + i
d.append(two)

print(d)

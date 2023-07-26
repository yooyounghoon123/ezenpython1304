# a = [1, 2, 3, 4]
# result=0
# for i in a:
#     print(i)
#
# a=[1,2,3,4]
# for i in a:
#     result=[i*2 for i in a]
# print(result)

a = []
b = []
c = []
d = []

a = [i for i in range(1, 6)]
b = [i for i in a if i % 2 == 0]
c = [i for i in a if i % 2 != 0]

print(a)
print(b)
print(c)

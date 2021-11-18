a = [[1], [2], [3]]
b = a[:]
# a.append([4])
# b.append([4])
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))
# print(id(a[3]))
# print(id(b[0]))
# print(id(b[1]))
# print(id(b[2]))
# print(id(b[3]))
a[0][0] = 0
print(a)
print(b)

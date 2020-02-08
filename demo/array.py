a = []

a.append(1)
a[0] = 2
a.remove(2)

print(a)

a.append(1)
a.append(2)
a.append(3)
a.append(0.1)


print(a) 

a.sort()

print(a)


print(a[1:3])
print(a[-3:])

print(a.index(0.1))
print(a.count(1))

a.append(1)
print(a.count(1))

a.extend([2,3])
print(a)

a.insert(0, 99)
print(a)

a.reverse()

print(a)

a.pop()

print(a)

a.pop(0)

print(a)

a.pop(-1)

print(a)




 




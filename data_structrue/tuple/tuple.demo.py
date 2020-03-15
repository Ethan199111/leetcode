a = (1, 'a')

print(a)

print(a[0])

print(a[1])

t = [(1,'a'), (2, 'b')]

print(t)

t.sort(key=lambda x: x[1], reverse=True)
print(t)

s = filter(lambda x: x[0] < 2, t)
print(list(s))

x = [1, 2, 3, 4, 5, 6]

r = (i for i in x if i % 2 == 0)

print(list(r))

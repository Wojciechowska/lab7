import numpy as np


a = np.array([10, 20, 30, 40])
b = np.array(4)


print(a)
print(b)
c = a + b
print(c)
print(b**2)
print(np.sin(a))
print(np.sqrt(a))


d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(d)
print(d.sum())
print(d.sum(axis=0))
print(d.sum(axis=1))
print(d.cumsum(axis=1))


a = np.array([[2, 1, 3], [-1, 2, 4]])
b = np.array([[1, 3], [2, -2], [-1, 4]])

c = np.dot(a, b)
print(c)
d = a.dot(b)
print(d)


a = np.arange(6).reshape((3,2))
print(a)
for b in a:
    print(b)
print("")
for c in range(0, a.shape[0], 1):
    for d in range(0, a.shape[1], 1):
        print(a[c][d])


for c in a.flat:
    print(c)

a = np.arange(6)
print(a)
print(a.shape)

b = a.reshape((2, 3))
print(c)
print(c.shape)
d = a.reshape((6, 1))
print(d)
print(d.shape)

e = c.ravel()
print(e)

print(c)
f = c.T
print(f)
print(f.shape)

a = np.array([0, 1, 2])
b = np.array([0, 1, 2])

c = np.dot(a, b)
print(c)
d = a * b
print(d)
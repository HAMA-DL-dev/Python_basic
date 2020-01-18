# range
print(tuple(range(10)))
print(tuple(range(0,8)))
print(tuple(range(0,9,2)))

# sequence
a=[1,2,3,4,5,6,7]

print(a[0:6])
print(a[:6])

print(a[:])

print(a[:-1])

print(a[-3:])

print(a[::2])


# str and sequence

a[::2]=['and','and','and','and']

print(a)

a[::2]=['and']*4

print(a)

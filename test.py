a=[1,[2,1],3]
b=a[:]

print('&a',id(a))
print('&a[0]',id(a[0]))
print('&a[1]',id(a[1]))
print('&a[1][0]',id(a[1][0]))
print('&a[1][1]',id(a[1][1]))


# print(id(a[1]))
# print(id(b[1]))

# print(id(a[1]))
# print(id(a[1][0]))
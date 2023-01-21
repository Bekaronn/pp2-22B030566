a = input()
b = input()
c = b.replace(b[0],a[0]) + ' ' + a.replace(a[0],b[0])
print(c)
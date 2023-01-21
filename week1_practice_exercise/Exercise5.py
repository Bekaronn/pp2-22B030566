a = (input()).split()
b = "I have "
for x in a:
    b += x
    if x==a[-1]:
        break
    b += ", "
print(b+" in my shopping cart.")
a = int(input())
b = int(input())
c = input()
if a==11 or a==12:
    if b>=900:
        if c == "true":
            print('Allowed')
        else:
            print("Not Allowed")
    else:
        print("Not Allowed")
elif a>=13 and a<=16:
    if b>=900:
        print('Allowed')
    else:
        print("Not Allowed")
elif a>=17 and a<=22:
    if b>=1400:
        print('Allowed')
    else:
        print("Not Allowed")
elif a>22:
    if b>=1900:
        print('Allowed')
    else:
        print("Not Allowed")
else:
    print("Not Allowed")
a = int(input())
b = int(input())
c = int(input())
if (a**2+b**2 == c**2):
    print("c is the triangle's hypotenuse")
    print("{}²+{}²={}²".format(a,b,c))
else:
    print("c is not the triangle's hypotenuse")

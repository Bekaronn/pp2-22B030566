# class String:
#     def getString(self, str):
#         self.str = str

#     def printString(self):
#         print((self.str).upper())

# st = String()
# st.getString(input())
# st.printString()



class Shape:
    x = 0
    y = 0
    cnt = 0
    def area(self):
        return self.x * self.y

    def printt(self):
        return self.cnt

    

class Square(Shape):
    def __init__(self,length):
        Shape.x = length
        Shape.y = self.x
        Shape.cnt +=1

class Rectangle(Shape):
    def __init__(self,length,width):
        Shape.x = length
        Shape.y = width
        Shape.cnt+=1


sq = Square(int(input()))
s = Shape()
print(s.area())

rc = Rectangle(int(input()),int(input()))
print(s.area())

s.area()
print(s.printt())


# class Point:
#     def move(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(str(self.x) + ' ' + str(self.y))

#     def dist(self):
#         print(abs(self.y-self.x))

# p = Point()

# p.move(1,2)
# p.show()
# p.dist()
# p.move(10,5)
# p.dist()

# def filter(ls):
#     l = []
#     for x in range(0,len(ls)):
#         for i in range(2,int(ls[x]/2)):
#             if ls[x]%i==0:
#                 t = False
#                 break
#         else:
#             l.append(ls[x])
#     return l


# ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# t = filter(ls)
# print(t)

# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def __str__(self):
#         return f'Owner: {self.owner}  Account balance: {self.balance}$'
        
#     def deposit(self,dep):
#         self.balance += dep
#         print('Deposit')
        
#     def withdraw(self,wid):
#         if self.balance >= wid:
#             self.balance -= wid
#             print('Withdraw')
#         else:
#             print('Not enough money')

# acc = Account("Beka", 100)
# acc.deposit(100)
# acc.withdraw(1000)
# print(acc)


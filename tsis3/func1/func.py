def conver(grams):
    return 28.3495231 * grams

print(conver(int(input())))

def calc(F):
    return (5 / 9) * (F - 32)

print(calc(int(input())))

def func(x,y):
    if(y/4==x):
        return y
    for i in range(0,y):
        x -= 1
        y -= 2
        if(y/4 == x):
            return x

x = int(input())
y = int(input())
h = func(x,y)
l = x-func(x,y)
print(h)
print(l)

def filter_prime(x):
    y = []
    for i in range(0,len(x)):
        u = True
        for j in range(2,int(x[i]/2)):
            if(x[i]%j==0):
                u = False
                break
        if u == True:
            y.insert(0,x[i])
        
    return y            
    
        
x = [1,2,3,4,5,6,7,8,9,10,11]
y = filter_prime(x)
print(y)

def rev(a):
    b = (a).split()
    s = ""
    for i  in range(0,len(b)):
        s += b[len(b)-i-1]
        s += " "

    return s

a = "We are ready"
b = rev(a)
print(b)

def num(a):
    for i in range(0,len(a)):
        if(a[i]==3):
            if(a[i+1]==3):
                return True
    return False
    

a = [1,3,3,1]
x = num(a)
print(x)

def spy_game(nums):
    x = 2
    y = 1
    for i in range(0,len(nums)):
        if(nums[i]==0):
            x-=1
        if(nums[i]==7 and x<=0):
            y-=1
    if x!=2 and y!=1:
        return True
    return False

print(spy_game([1,2,4,0,0,7,5]))

print(spy_game([1,0,2,4,0,5,7]))

print(spy_game([1,7,2,0,4,5,0]))

import math

def comp(a):
    return (4*math.pi*(a**3))/3

print(comp(5))

def uni(x):
    y = [x[0],]
    for i range(0,len(x)):
        if

x = uni([3,3,3,4,1,3,7,8,1,9,3,3,4,5,0,4,10])
print(x)

def palind(s):
    size = int(len(s)/2)
    for i in range(0,size):
        if(s[i]!=s[len(s)-i-1]):
            return False
    return True

x = input()
print(palind(x))

def histo(x):
    for i in range(0,len(x)):
        for j in range(0,x[i]):
            print('*', end="")
        print()

histo([5,6,3])

x = True
name = input("Hello what is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
y = random.randint(1,20)
cnt = 0;
while x:
    num = int(input())
    cnt += 1
    if(num > y):
        print("Your guess is to big")
        print("Take a guess")
    elif(num < y):
        print("Your guess is to low")
        print("Take a guess")
    else:
        print(f"Good job, KBTU! You guessed my number in {cnt} guesses!")
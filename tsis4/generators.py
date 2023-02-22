#1. Create a generator that generates the squares of numbers up to some number N.
import math

class Solution:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < self.n:
            x = self.a
            self.a = math.sqrt(self.a)
            self.a += 1
            self.a *= self.a 
            return x
        else:
            raise StopIteration

n = int(input())

gen = Solution(n)
myiter = iter(gen)

for x in myiter:
    print(x)

#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

class Solution:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= self.n:
            x = self.a 
            self.a += 1
            return x
        else:
            raise StopIteration

n = int(input())

s = Solution(n)
myiter = iter(s)
lin = []

for x in myiter:
    lin.append(x)

print(lin)

#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

class Solution:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a < self.n:
            x = self.a
            self.a += 1
            if (x%3==0 or x%4==0):
                return x
            else:
                return 0
        else:
            raise StopIteration

n = int(input())

s = Solution(n)
myiter = iter(s)

for x in myiter:
    if x != 0:
        print(x)

#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

class squares:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        self.x = a
        return self

    def __next__(self):
        if self.a <= self.b:
            s = self.a * self.a
            self.a+=1
            return s
        else:
            raise StopIteration

a = int(input())
b = int(input())

square = squares(a,b)
myiter = iter(square)

for x in myiter:
    print(x)

#5. Implement a generator that returns all numbers from (n) down to 0.

class Solution:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.a = self.n
        return self

    def __next__(self):
        if self.a >= 0:
            x = self.a
            self.a -= 1
            return x
        else:
            raise StopIteration

n = int(input())

s = Solution(n)
myiter = iter(s)

for x in myiter:
    print(x)
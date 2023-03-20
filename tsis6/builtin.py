#1. Write a Python program with builtin function to multiply all the numbers in a list

# from functools import reduce
# l = [1,2,3,4,5,6]
# print(reduce(lambda x, y: x*y, l))

#2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

# str = "FADsdakfjdsfadfdsfASDFsdafsdafasdFsadfASDf"

# cnt1 = 0
# cnt2 = 0

# for x in str:
#     if(x.isupper()):
#         cnt1 += 1
#     else:
#         cnt2 += 1

# print("Upper:", cnt1)
# print("Lower:", cnt2)

#3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.

# str = "ABBCQCBBA"
# t = True

# for x in range(0,round(len(str)/2)):
#     if str[x] is not str[len(str)-x-1]:
#         print("not palindrome")
#         t = False
#         break

# if t:
#     print("palindrome")

#4. Write a Python program that invoke square root function after specific milliseconds.

# from time import sleep
# import math

# def delay(ms, num):
#     sleep(ms / 1000)
#     return math.sqrt(num)

# num = int(input())
# ms = int(input())

# x = (delay(ms,num))
# print("Square root of {} after {} miliseconds is {}".format(num, ms, x))

#5. Write a Python program with builtin function that returns True if all elements of the tuple are true.

# x = [True, True, True]
# print(all(x))
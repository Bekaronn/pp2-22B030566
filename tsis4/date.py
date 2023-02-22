import datetime

#1. Write a Python program to subtract five days from current date.

x = datetime.datetime.now()
y = datetime.timedelta(days=5)

print(x-y)

#2. Write a Python program to print yesterday, today, tomorrow.

x = datetime.datetime.now()

print(x -  datetime.timedelta(days=1))
print(x)
print(x +  datetime.timedelta(days=1))

#3. Write a Python program to drop microseconds from datetime.

x = datetime.datetime.now()

print(x.replace(microsecond=0))

#4. Write a Python program to calculate two date difference in seconds.

x = datetime.datetime(2021, 10, 20)
y = datetime.datetime(2020, 12, 2)
print((x-y).total_seconds())
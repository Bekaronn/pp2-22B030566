import math
number = int(input())
var = input()
if not((var).isdigit()):
    print(var*number)
else:
    print(math.ceil(int(var)/number))

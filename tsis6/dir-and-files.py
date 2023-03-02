#1. Write a Python program to list only directories, files and all directories, files in a specified path.

import os

path = 'dir'

print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print(os.listdir(path))

#2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os
print('Exist:', os.access('dir/w.txt', os.F_OK))
print('Readable:', os.access('dir/w.txt', os.R_OK))
print('Writable:', os.access('dir/w.txt', os.W_OK))
print('Executable:', os.access('dir/w.txt', os.X_OK))

#3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os
print("Test a path exists or not:")
path = r'dir/w.txt'
print(os.path.exists(path))

print("File name of the path:")
print(os.path.basename(path))
print("Dir name of the path:")
print(os.path.dirname(path))

#4. Write a Python program to count the number of lines in a text file.

p = open("dir/w.txt","r")
cnt = 0

for x in p.readlines():
    cnt += 1

print(cnt)

p.close()

#5. Write a Python program to write a list to a file.

number = [1,2,3,4,5,6,7,8,9]

p = open("dir/1.txt","w")
for x in number:
    p.write("%s\n" % x)
p.close()

p = open('dir/1.txt')
print(p.read())

p.close()

#6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt


for x in range(0,26):
    letter = chr(65+x)
    p = open(f"letter/{letter}.txt", "w")

#7. Write a Python program to copy the contents of a file to another file

first = open("dir/1.txt","r")
second = open("letter/a.txt","w")

for x in first.readlines():
    second.write(x)

#8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os 

if os.path.exists("dir/2.txt"):
    os.remove("dir/2.txt")
else:
    print("File doesn't exist")
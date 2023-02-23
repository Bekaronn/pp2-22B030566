#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# import re
# my_string = input()
# m = re.search('ab*?', my_string)

# if m:
#     print('it\'s a match')
# else:
#     print('no match found')

#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

# import re
# my_string = input()
# m = re.search('ab{2,3}?',my_string)

# if m:
#     print('it\'s a match')
# else:
#     print('no match found')

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.

# import re
# my_string = input()
# m = re.search('[a-z]+_[a-z]', my_string)
# if m:
#     print('it\'s a match')
# else:
#     print('no match found')

#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# import re
# my_string = input()
# m = re.search('[A-Z]+[a-z]', my_string)
# if m:
#     print('it\'s a match')
# else:
#     print('no match found')

#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# import re
# my_string = input()
# m = re.search('a.*?b$', my_string)
# if m:
#     print('it\'s a match')
# else:
#     print('no match found')

#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# import re

# my_string = input()
# replace = input()

# results = re.sub("[ ,.:]",replace, my_string)
# print(results)

#7. Write a python program to convert snake case string to camel case string.

# import re

# def camel(match):
#     return match.group(1) + match.group(2).upper()

# my_string = input()

# results = [re.sub("(.*?)_([a-zA-Z])", camel, my_string, 0)]
# print(results)

#8. Write a Python program to split a string at uppercase letters.

# import re

# my_string = input()

# results = re.split('(?<=.)(?=[A-Z])', my_string)
# print(results)

#9. Write a Python program to insert spaces between words starting with capital letters.

# import re 

# my_string = input()

# results = re.findall("[A-Z][a-z]*", my_string)
# print(' '.join(results))

#.10 Write a Python program to insert spaces between words starting with capital letters.

# import re

# def snake(match):
#     return match.group(1).lower() + '_' + match.group(2).lower()

# my_string = input()

# results = [re.sub("(.+?)([A-Z])", snake, my_string, 0)]
# print(results)

import re

txt = input()
regex = re.sub('[, .]', ":", txt)
print(regex)

# код заменяет все вхождения пробелов, запятых или точек в строке на двоеточие.
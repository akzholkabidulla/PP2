import re

message = input()
result = re.findall("[A-Z][a-z]*", message)
print(' '.join(result))

#  вставкa пробелов между словами, начинающимися с заглавных букв.
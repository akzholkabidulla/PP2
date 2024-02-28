import re

message = input()
result = re.findall("[A-Z][^A-Z]*", message)
print(result)

# разделяет строку на подстроки в местах, где встречаются заглавные буквы.
# input : MyNameIsAkzhol
# output : 'My' , 'Name' , 'Is' , 'Akzhol'
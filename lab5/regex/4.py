import re

txt = input("Введите строку: ")
pattern = r"[A-Z][a-z]*"
found_sequences = re.findall(pattern, txt)
if found_sequences:
    print("Найденные последовательности:")
    for sequence in found_sequences:
        print(sequence)
else:
    print("NONE")

#  Найдем последовательностей из одной заглавной буквы, за которой следуют строчные буквы.
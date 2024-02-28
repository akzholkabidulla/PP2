import re

txt = input("Введите строку: ")
pattern = "^a.*?b$"
found_sequences = re.findall(pattern, txt)
if found_sequences:
    print("Найденные последовательности:")
    for sequence in found_sequences:
        print(sequence)
else:
    print("NONE")


# мы ищем строки, которые начинаются с 'a', после которого могут идти любые символы, и заканчиваются на 'b'.
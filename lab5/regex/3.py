import re

txt = input("Введите строку: ")
pattern = r'[a-z]+_[a-z]+'
found_sequences = re.findall(pattern, txt)
if found_sequences:
    print("Найденные последовательности строчных букв:")
    for sequence in found_sequences:
        print(sequence)
else:
    print("Последовательностей строчных букв с подчеркиванием не найдено.")


# Этот код найдет все последовательности строчных букв, которые разделены символом подчеркивания ('_')
import os

path1 = r"C:\Users\User\OneDrive\Рабочий стол\pp2\lab6\dir_and_files\a.txt"
path2 = r"C:\Users\User\OneDrive\Рабочий стол\pp2\lab6\dir_and_files\b.txt"

temp1 = open(path1, "r")
temp2 = open(path2, "w")

for i in temp1:
    temp2.write(str(i))
temp1.close()
temp2.close()

temp2 = open(path2, "r")
for i in temp2:
    print(i)

# для копирования содержимого файла в другой файл
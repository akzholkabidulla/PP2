import os

path1 = input()
path2 = input()

temp1 = open(path1, "r")
temp2 = open(path2, "w")

for i in temp1:
    temp2.write(i) # Этот цикл читает каждую строку из файла t1 и записывает ее в файл t2.
temp1.close()
temp2.close()

temp2 = open(path2, "r")
for i in temp2:
    print(i)

# для копирования содержимого файла в другой файл
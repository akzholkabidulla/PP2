import os

path = input()
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print('is not exist')   

#проверить, существует данный путь или нет. 
#Если путь существует, найдите имя файла и часть каталога данного пути.
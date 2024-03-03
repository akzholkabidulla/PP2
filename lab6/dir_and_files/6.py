import os

for i in range(65, 91):
    letter = chr(i)
    f = open(letter +'.txt', 'w')
    f.close()

#os.remove(letter + '.txt')
    
# для создания 26 текстовых файлов с именами A.txt, B.txt и так далее до Z.txt

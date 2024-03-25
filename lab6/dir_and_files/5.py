arr = list(map(str, input().split()))
with open('input2.txt', 'w') as f:
    for i in arr:
        f.write(i)
        f.write('\n')

with open('input2.txt', 'r') as r:
    x = r.read()
print(x)  

# для записи списка в файл.
# ввод : слова через пробел 
# output: код выводит их в файле "input2.txt"

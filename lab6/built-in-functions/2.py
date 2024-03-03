ako = input()

upper = 0
lower = 0

for i in ako:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1

print(upper,lower)

# Количество прописных и строчных букв

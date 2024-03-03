a = input()
b = a.split()
b = [c.lower()=='true' for c in b]

print(all(b))

#  Bозвращает значение True, если все элементы кортежа равны true.
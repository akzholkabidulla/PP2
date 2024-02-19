def squares (a,b):
    for i in range(a,b+1):
        a=pow(i,2)
        yield a
        a += 1

result =  squares(int(input("for this number:")),int(input("to this number:")))

for x in result:
    print(x)
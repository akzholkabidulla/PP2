#print(*[pow(x,2) for x in range(1,int(input()))])

#ex1
def squares1(n):
    for x in range(1, n + 1):
        if x * x > n:
            break
        yield x * x

a = int(input())
for x in squares1(a):
    print(x)

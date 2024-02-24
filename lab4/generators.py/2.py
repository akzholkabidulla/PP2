#print(*[x for x in range(0,int(input())+1) if x%2==0])

#ex2
def even_num(num):
    even = (int(i) for i in range(0, num + 1, 2))
    for x in range(int(num / 2)):
        print(next(even), end = ", ")
    print(next(even))

b = int(input())
even_num(b)

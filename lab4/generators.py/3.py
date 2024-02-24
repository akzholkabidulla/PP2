#print(*[x for x in range(int(input())+1)if x%3==0 and x%4==0])

def divisible(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i 
c = int(input())
for num in divisible(c):
    print(num)

#print(*[i for i in reversed(range(int(input())+1))])

def downto(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in downto(n):
    print(num)
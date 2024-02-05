def has_33(a):
    result = False
    for i in range(len(a)-1):
        if a[i] == a[i+1] == '3':
            result = True
            break
    print(result)

a = input().split()
has_33(a)

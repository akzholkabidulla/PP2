def uniq(a):
    unique_values = []

    for i in range(len(a)):
        is_unique = True
        for j in range(i + 1, len(a)):
            if int(a[i]) == int(a[j]):
                is_unique = False
                break
        if is_unique:
            unique_values.append(int(a[i]))

    print(*unique_values)

if __name__ == '__main__':
    a = input().split()
    uniq(a)

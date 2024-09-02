def find_num(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return f'{n} - {result}'

for k in range(3, 20):
    print(find_num(k))
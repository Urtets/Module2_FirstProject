def get_matrix(n, m, value):
    matrix = []
    if value == 0 or value < 0: # В случае передачи аргумента со значением 0 или меньше, будет возвращаться пустой список
        return matrix
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

result1 = get_matrix(2, 15, -50)
result2 = get_matrix(10, 8, 1)
result3 = get_matrix(5, 5, 0)
print(result1)
print(result2)
print(result3)
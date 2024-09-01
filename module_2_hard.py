import random

random_int = random.randint(3, 20)
num_1 = 4
print(num_1)
def find_num2(a):
    b = ""
    for i in range(1, a + 1):
        if i == a:
            b = b + str(i)
        for j in range(1, a + 1):
            print(f'Первое число {i}, второе число {j}')
            c = i + j
            print(f'Число {c}')
            if a % c == 0 and j < i:
                b = b + str(i) + "+" + str(j) + " "

    return b

print(find_num2(num_1))
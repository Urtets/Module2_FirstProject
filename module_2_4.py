numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = []
not_prime_numbers = []
for i in range(len(numbers)):
    if numbers[i] > 1:
        for j in range(2, (numbers[i] // 2) + 1):
            if numbers[i] % j == 0:
                not_prime_numbers.append(numbers[i])
                break
        else:
            prime_numbers.append(numbers[i])


print(prime_numbers)
print(not_prime_numbers)
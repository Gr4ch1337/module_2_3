numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    elif i == 2:
        primes.append(i)
        continue
    for j in range(2, i):
        is_prime = i % j != 0
        if j == i - 1:
            primes.append(i)
        if is_prime == False:
            not_primes.append(i)
            break
print('Простые: ', primes)
print('Составные: ', not_primes)

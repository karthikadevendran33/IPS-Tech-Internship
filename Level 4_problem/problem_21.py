def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_two_digit_primes():
    count = 0
    for num in range(10, 100):
        if is_prime(num):
            count += 1
    return count

answer = count_two_digit_primes()
print(answer)

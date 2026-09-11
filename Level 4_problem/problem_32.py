def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def count_primes_with_digit_sum_14():
    count = 0
    for num in range(2, 1000000):
        if digit_sum(num) == 14 and is_prime(num):
            count += 1
    return count

answer = count_primes_with_digit_sum_14()
print(answer)

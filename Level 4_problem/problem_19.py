def sum_odd_numbers():
    total = 0
    for num in range(100, 1000):
        if num % 2 != 0:
            total += num
    return total

answer = sum_odd_numbers()
print(answer)

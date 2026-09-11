def sum_odd_numbers():
    total = 0
    for num in range(10, 100):
        if num % 2 != 0:
            total += num
    return total

answer = sum_odd_numbers()
print(answer)

def sum_odd_numbers():
    total = 0
    for num in range(1, 10, 2):
        total += num
    return total

answer = sum_odd_numbers()
print(answer)

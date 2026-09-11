def count_odd_numbers():
    count = 0
    for num in range(10, 100):
        if num % 2 != 0:
            count += 1
    return count

answer = count_odd_numbers()
print(answer)

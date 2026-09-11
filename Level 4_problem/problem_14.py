def count_odd_numbers():
    count = 0
    for num in range(1, 10, 2):
        count += 1
    return count

answer = count_odd_numbers()
print(answer)

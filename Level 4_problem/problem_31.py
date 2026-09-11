def count_zeroes():
    count = 0
    for num in range(1, 1001):
        count += str(num).count("0")
    return count

answer = count_zeroes()
print(answer)

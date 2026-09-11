def is_non_decreasing(num):
    digits = str(num)
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True

def count_non_decreasing_numbers():
    count = 0
    for num in range(1000, 10000):
        if is_non_decreasing(num):
            count += 1
    return count

answer = count_non_decreasing_numbers()
print(answer)

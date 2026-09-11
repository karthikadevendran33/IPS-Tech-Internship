count = 0
for i in range(100000):
    num = i
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10

    if sum == 14:
        count = count + 1

print(count)
def digit_sum(num):
    return num // 100 + (num // 10) % 10 + num % 10

num = int(input("Enter a three-digit number: "))
answer = digit_sum(num)
print(answer)

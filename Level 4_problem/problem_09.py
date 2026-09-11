def digit_sum(num):
    return num // 10 + num % 10

num = int(input("Enter a two-digit number: "))
answer = digit_sum(num)
print(answer)

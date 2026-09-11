def tens_digit(num):
    return (num // 10) % 10

num = int(input("Enter a three-digit number: "))
answer = tens_digit(num)
print(answer)

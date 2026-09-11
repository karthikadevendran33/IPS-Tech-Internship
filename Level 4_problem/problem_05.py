def hundreds_digit(num):
    return (num // 100) % 10

num = int(input("Enter a three-digit number: "))
answer = hundreds_digit(num)
print(answer)

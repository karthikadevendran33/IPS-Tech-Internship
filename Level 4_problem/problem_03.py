def ones_digit(num):
    return num % 10

num = int(input("Enter a three-digit number: "))
answer = ones_digit(num)
print(answer)

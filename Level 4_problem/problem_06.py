def reverse_number(num):
    ones = num % 10
    tens = num // 10
    return ones * 10 + tens

num = int(input("Enter a two-digit number: "))
answer = reverse_number(num)
print(answer)

num = int(input("Enter a Number: "))
sum = num // 100 + (num // 10) % 10 + num % 10

while sum >= 10:
    sum = sum // 10 + sum % 10

print(sum)
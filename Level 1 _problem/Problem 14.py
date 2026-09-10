num = int(input("Enter a Number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
print(c * 100 + b * 10 + a)
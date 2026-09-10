num = int(input("Enter a Number: "))
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 1
print(a * 1000 + b * 100 + d * 10 + c)
num = int(input("Enter a Number: "))
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
print(b * 1000 + a * 100 + c * 10 + d)
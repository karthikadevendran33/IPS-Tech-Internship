num = int(input("Enter a Number: "))
a = (num // 100) % 10
b = (num // 10) % 10
print(num - (a == b) * 5)
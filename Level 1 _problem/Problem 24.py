num = int(input("Enter a Number: "))
a = num // 100
b = num % 10
print(num - (a == b) * 5)
num = int(input("Enter a Number: "))
a = num // 10
b = num % 10
print(num - ((a + b) % 2 == 1) * 5)
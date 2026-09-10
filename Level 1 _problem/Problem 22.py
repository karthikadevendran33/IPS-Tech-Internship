num = int(input("Enter a Number: "))
a = (num // 10) % 10
print(num - (a % 2 == 1) * 5)
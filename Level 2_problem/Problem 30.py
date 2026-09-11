a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    num = a
else:
    num = b
while num > 0:
    if a % num == 0 and b % num == 0:
        print(num)
        break

    num = num - 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    num = a
else:
    num = b
while True:
    if num % a == 0 and num % b == 0:
        print(num)
        break

    num = num + 1
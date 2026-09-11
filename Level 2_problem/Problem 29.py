a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
num = max(a, b, c)

while True:
    if num % a == 0 and num % b == 0 and num % c == 0:
        print(num)
        break

    num = num + 1
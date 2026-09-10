num = int(input("Enter a Number: "))
a = num // 100
b = num % 10
if a + b < 10:
    print("Success")
else:
    print("Failure")
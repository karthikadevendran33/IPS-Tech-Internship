num = int(input("Enter a Number: "))
a = num // 10
b = num % 10
if a + b == 10:
    print("Success")
else:
    print("Failure")
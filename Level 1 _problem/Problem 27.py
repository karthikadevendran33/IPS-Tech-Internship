num = int(input("Enter a Number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
if a + b + c == 10:
    print("Success")
else:
    print("Failure")
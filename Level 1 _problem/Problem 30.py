num = int(input("Enter a Number: "))
a = (num // 100) % 10
b = (num // 10) % 10
if a + b == 10 and (a > 7 or b > 7):
    print("Success")
else:
    print("Failure")
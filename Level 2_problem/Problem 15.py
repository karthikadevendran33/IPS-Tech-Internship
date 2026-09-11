num = input("Enter a number: ")
a = int(num[0])
if a % 2 != 0:
    a = a - 1
print(str(a) + num[1:])
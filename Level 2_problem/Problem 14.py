num = input("Enter a number: ")
a = num[0]
b = num[-1]
result = b + num[1:-1] + a
print(result)
def add_large_numbers(num1, num2):
    return str(int(num1) + int(num2))

num1, num2 = input("Enter two numbers: ").split()
answer = add_large_numbers(num1, num2)
print(answer)

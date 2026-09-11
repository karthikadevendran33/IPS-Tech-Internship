def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter a number: "))
answer = reverse_number(num)
print(answer)

def reverse_number(num):
    return (num % 10) * 100 + ((num // 10) % 10) * 10 + num // 100

num = int(input("Enter a three-digit number: "))
answer = reverse_number(num)
print(answer)

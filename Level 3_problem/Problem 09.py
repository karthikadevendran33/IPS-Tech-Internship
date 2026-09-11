def swap_digits(num):
    a = num // 10
    b = num % 10
    result = b * 10 + a
    print(result)

num = int(input("Enter a two-digit number: "))
swap_digits(num)
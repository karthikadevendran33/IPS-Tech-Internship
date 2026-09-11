def check_sum(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    if sum == 14:
        print("Sum of Digits is 14")
    else:
        print("Sum of Digits is not 14")
num = int(input("Enter a number: "))
check_sum(num)
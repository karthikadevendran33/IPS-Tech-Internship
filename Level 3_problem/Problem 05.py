def count_zero(num):
    count = 0
    while num > 0:
        digit = num % 10

        if digit == 0:
            count = count + 1

        num = num // 10
    print(count)

num = int(input("Enter a number: "))
count_zero(num)
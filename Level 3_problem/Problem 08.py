def check_ascending(num):
    last = num % 10
    num = num // 10
    result = "Yes"

    while num > 0:
        digit = num % 10

        if digit >= last:
            result = "No"
            break

        last = digit
        num = num // 10
    print(result)

num = int(input("Enter a number: "))
check_ascending(num)
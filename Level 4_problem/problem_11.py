def digit_sum(num):
    return sum(int(digit) for digit in str(num))

num = int(input("Enter a four-digit number: "))
answer = digit_sum(num)
print(answer)

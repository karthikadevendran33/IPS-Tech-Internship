def check_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print("Number is Prime")
    else:
        print("Number is not Prime")

num = int(input("Enter a number: "))
check_prime(num)
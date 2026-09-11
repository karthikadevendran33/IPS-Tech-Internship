num = int(input("Enter a number: "))
count = 0
sum = 0
temp = num
for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1
while temp > 0:
    sum = sum + temp % 10
    temp = temp // 10

prime = count == 2

if prime and sum == 14:
    print("Prime & Sum of Digits is 14")
elif not prime and sum == 14:
    print("Not Prime but sum of digits is 14")
elif prime:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime and sum of Digits is not 14")
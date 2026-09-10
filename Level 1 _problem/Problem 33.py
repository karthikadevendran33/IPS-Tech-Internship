num1, num2 = map(int, input().split())
if num1 > num2:
    num = num1
else:
    num = num2
sum = num // 10 + num % 10
print(sum) 
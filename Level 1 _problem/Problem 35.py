num1, num2 = map(int, input().split())
a = num1 // 100 + num1 % 10
b = num2 // 100 + num2 % 10
if a > b:
    num = num1
else:
    num = num2
sum = num // 100 + (num // 10) % 10 + num % 10
print(sum)
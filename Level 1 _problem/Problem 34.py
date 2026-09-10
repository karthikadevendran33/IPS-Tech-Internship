num1, num2 = map(int, input().split())
a = (num1 // 10) % 10
b = (num2 // 10) % 10
if a > b:
    num = num1
else:
    num = num2
sub = num // 100 - num % 10
print(abs(sub))
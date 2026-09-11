num = int(input("Enter a number: "))
a = num % 100
count = 0
for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
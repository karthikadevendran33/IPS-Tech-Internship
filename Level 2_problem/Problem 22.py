num = input("Enter a number: ")
count = 0
for i in range(len(num) - 1):
    a = int(num[i:i+2])

    if a >= 10 and a % 2 != 0:
        count = count + 1
print(count)
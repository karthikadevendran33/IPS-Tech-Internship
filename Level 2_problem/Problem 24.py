num = input("Enter a number: ")
count = 0
for i in range(len(num) - 1):
    a = int(num[i:i+2])

    if a == 16 or a == 25 or a == 36 or a == 49 or a == 64 or a == 81:
        count = count + 1

print(count)
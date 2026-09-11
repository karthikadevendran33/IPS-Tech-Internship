num = input("Enter a number: ")
count = 0
for i in num:
    a = int(i)

    if a == 1 or a == 4 or a == 9:
        count = count + 1

print(count)
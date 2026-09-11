num = input("Enter a number: ")
count = 0
for i in num:
    a = int(i)

    if a == 2 or a == 3 or a == 5 or a == 7:
        count = count + 1
print(count)
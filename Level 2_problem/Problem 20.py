count = 0
for i in range(1, 10):
    if i > 1:
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False

        if prime:
            count = count + 1

print(count)
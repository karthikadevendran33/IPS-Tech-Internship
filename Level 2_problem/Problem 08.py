for i in range(10, 100):
    if i % 2 == 0:
        a = i // 10
        b = i % 10
        if a + b == 6:
            print(i)
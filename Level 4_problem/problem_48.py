def adjust_carry(array):
    for i in range(len(array) - 1, 0, -1):
        carry = array[i] // 10
        array[i] = array[i] % 10
        array[i - 1] += carry

    return array

array = list(map(int, input("Enter array values: ").split()))
answer = adjust_carry(array)
print(*answer)

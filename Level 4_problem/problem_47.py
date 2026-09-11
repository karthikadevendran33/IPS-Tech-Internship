def add_integer_arrays(array1, array2):
    max_length = max(len(array1), len(array2))
    result = [0] * max_length

    array1 = [0] * (max_length - len(array1)) + array1
    array2 = [0] * (max_length - len(array2)) + array2

    for i in range(max_length):
        result[i] = array1[i] + array2[i]

    return result

array1 = list(map(int, input("Enter first array: ").split()))
array2 = list(map(int, input("Enter second array: ").split()))

answer = add_integer_arrays(array1, array2)
print(answer)

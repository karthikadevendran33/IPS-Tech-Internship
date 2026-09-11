def integer_array_to_char_array(array):
    return "".join(str(digit) for digit in array)

array = list(map(int, input("Enter integer array: ").split()))
answer = integer_array_to_char_array(array)
print(answer)

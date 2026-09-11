def string_to_integer_array(number_string):
    return [int(digit) for digit in number_string]

number_string = input("Enter a number string: ")
answer = string_to_integer_array(number_string)
print(answer)

def remove_leading_zeroes(number_string):
    result = number_string.lstrip("0")
    if result == "":
        return "0"
    return result

number_string = input("Enter a number string: ")
answer = remove_leading_zeroes(number_string)
print(answer)

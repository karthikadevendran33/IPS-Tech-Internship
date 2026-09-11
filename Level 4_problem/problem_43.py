def is_valid_number(text):
    if text == "":
        return False
    return text.isdigit()

text = input("Enter a string: ")

if is_valid_number(text):
    print("Valid Number")
else:
    print("Not a Valid Number")

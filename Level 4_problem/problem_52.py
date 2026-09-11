def find_substring_position(text, substring):
    position = text.find(substring)
    if position == -1:
        return -1
    return position + 1

text = input("Enter main string: ")
substring = input("Enter substring: ")

answer = find_substring_position(text, substring)
print(answer)

def find_character_positions(text, char):
    positions = []
    for i in range(len(text)):
        if text[i] == char:
            positions.append(i + 1)
    return positions

text = input("Enter a string: ")
char = input("Enter a character: ")

answer = find_character_positions(text, char)
print(", ".join(map(str, answer)))

def count_words(text):
    return len(text.split())

text = input("Enter a string: ")
answer = count_words(text)
print(answer)

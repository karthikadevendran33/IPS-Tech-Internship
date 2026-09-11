def is_palindrome(num):
    text = str(num)
    return text == text[::-1]

def count_palindromes():
    count = 0
    for num in range(1, 100000):
        if is_palindrome(num):
            count += 1
    return count

answer = count_palindromes()
print(answer)

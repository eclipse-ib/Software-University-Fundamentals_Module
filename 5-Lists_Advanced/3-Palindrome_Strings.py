def is_palindrom(word):
    return word == word[::-1]


words = input().split()
key_word = input()

palindromes = [word for word in words if is_palindrom(word)]
print(f"{palindromes}\nFound palindrome {palindromes.count(key_word)} times")
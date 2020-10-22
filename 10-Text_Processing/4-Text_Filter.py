banned_words = input().split(", ")
sentences = input()

for word in banned_words:
    sentences = sentences.replace(word, ("*" * len(word)))

print(sentences)
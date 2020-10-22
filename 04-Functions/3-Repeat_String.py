def new_string(word: str, repeat: int):
    return word * repeat


word = input()
repeat = int(input())
print(new_string(word, repeat))
text = "".join(input().split())

for index,emoticon in enumerate(text):
    if emoticon == ":":
        print(f"{emoticon+text[index+1]}")

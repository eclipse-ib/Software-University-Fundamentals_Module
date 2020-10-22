char_1: str = input()
char_2: str = input()


def between_char(char_1, char_2):
    new_string = ""
    for i in range(ord(char_1)+1, ord(char_2)):
        new_string += " " + chr(i)
    return new_string


print(between_char(char_1, char_2))

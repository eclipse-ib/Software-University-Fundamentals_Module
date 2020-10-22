password = input()


def pass_len(password):
    if not 6 <= len(password) <= 10:
        return "Password must be between 6 and 10 characters"


def pass_content(password):
    count_cont = 0
    for i in password:
        # if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        # Нов по-хитър вариант на горното:
        if i.isdigit() or i.isalpha():
            count_cont += 1
    if len(password) != count_cont:
        return "Password must consist only of letters and digits"


def pass_digits(password):
    count_digits = 0
    for j in password:
        if j.isdigit():
            count_digits += 1
    if count_digits < 2:
        return "Password must have at least 2 digits"


def_errors = [
    pass_len,
    pass_content,
    pass_digits
]
count_errors = 0
for i in def_errors:
    if i is not None:
        print(i)
        count_errors += 1
if count_errors == 0:
    print(f"Password is valid")
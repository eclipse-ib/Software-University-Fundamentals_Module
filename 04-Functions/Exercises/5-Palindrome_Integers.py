numbers = input().split(", ")


for i in numbers:

    def is_palindrome(numbers):
        rev = ""
        for j in i:
            rev = j + rev
        if rev == i:
            return True
        else:
            return False


    print(is_palindrome(numbers))

def the_smallest(int_1, int_2, int_3):
    number = int_3
    if int_1 < int_2 and int_1 < int_3:
        number = int_1
    elif int_2 < int_1 and int_2 < int_3:
        number = int_2
    return number


int_1: int = int(input())
int_2: int = int(input())
int_3: int = int(input())
print(the_smallest(int_1, int_2, int_3))
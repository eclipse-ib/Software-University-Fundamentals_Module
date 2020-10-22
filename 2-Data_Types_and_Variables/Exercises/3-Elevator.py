# Кратък вариант без if проверки:
import math
n = int(input())
p = int(input())

elevator_curses = math.ceil(n / p)
print(elevator_curses)



# Дълъг вариант с if проверки
# n = int(input())
# p = int(input())
#
# full_elevator_curses = n // p
#
# if n % p == 0:
#     print(f"{full_elevator_curses}")
# elif n > p:
#     print(f"{full_elevator_curses+1}")
# elif n < p:
#     print(f"{full_elevator_curses}")

# Вариант с повечето данни за принт:
# n = int(input())
# p = int(input())
#
# full_elevator_curses = n // p
# not_full_elevator_curses = n % p
#
# if n % p == 0:
#     print(f"{full_elevator_curses} courses * {p} people")
# elif n > p:
#     print(f"{full_elevator_curses} courses * {p} people")
#     print(f"+{not_full_elevator_curses} * {p} people")
# elif n < p:
#     print(f"All the persons fit inside in the elevator.")
#     print(f"Only one course is needed.")
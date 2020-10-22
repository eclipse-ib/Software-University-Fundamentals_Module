numbers = input().split(" ")

while True:
    command = input()
    if command == "end":
        break
    list_command = command.split()

    if "exchange" in command:
        def exchange(numbers):
            if int(list_command[1]) < 0 or int(list_command[1]) >= len(numbers):
                return "Invalid index"
            list_one = []
            list_two = []
            for i, j in enumerate(numbers, 0):

                if i > int(list_command[1]):
                    list_two.append(j)
                else:
                    list_one.append(j)
            list_after_exchange = list_two + list_one
            # new_str = " ".join(list_after_exchange)
            return list_after_exchange


        if exchange(numbers) == "Invalid index":
            print(f"Invalid index")
        else:
            numbers = exchange(numbers)


    elif "max" in command:
        if list_command[1] == "even" or list_command[1] == "odd":
            def max_even_odd(numbers):
                max_even = 0
                max_even_ind = None
                max_odd = 0
                max_odd_ind = None
                for ind, even_odd in enumerate(numbers, 0):
                    if int(even_odd) % 2 == 0:
                        if int(even_odd) >= max_even:
                            max_even = int(even_odd)
                            max_even_ind = ind
                    else:
                        if int(even_odd) >= max_odd:
                            max_odd = int(even_odd)
                            max_odd_ind = ind
                if list_command[1] == "even":
                    if max_even_ind == None:
                        return "No matches"
                    else:
                        return max_even_ind
                else:
                    if max_odd_ind == None:
                        return "No matches"
                    else:
                        return max_odd_ind


            print(max_even_odd(numbers))


    elif "min" in command:
        if list_command[1] == "even" or list_command[1] == "odd":
            def min_even_odd(numbers):
                min_even = 1000
                min_even_ind = None
                min_odd = 1000
                min_odd_ind = None
                for ind, even_odd in enumerate(numbers, 0):
                    if int(even_odd) % 2 == 0:
                        if int(even_odd) <= min_even:
                            min_even = int(even_odd)
                            min_even_ind = ind
                    else:
                        if int(even_odd) <= min_odd:
                            min_odd = int(even_odd)
                            min_odd_ind = ind
                if list_command[1] == "even":
                    if min_even_ind == None:
                        return "No matches"
                    else:
                        return min_even_ind
                else:
                    if min_odd_ind == None:
                        return "No matches"
                    else:
                        return min_odd_ind


            print(min_even_odd(numbers))


    elif "first" in command:
        if list_command[2] == "even" or list_command[2] == "odd":
            def first_count(numbers):
                if int(list_command[1]) > len(numbers):
                    return "Invalid count"
                first_count_list_even = []
                first_count_list_odd = []
                for first_counts in (numbers):
                    if list_command[2] == "even":
                        if len(first_count_list_even) == int(list_command[1]):
                            break
                        if int(first_counts) % 2 == 0:
                            first_count_list_even.append(int(first_counts))
                    else:
                        if len(first_count_list_odd) == int(list_command[1]):
                            break
                        if int(first_counts) % 2 != 0:
                            first_count_list_odd.append(int(first_counts))
                if list_command[2] == "even":
                    return first_count_list_even
                else:
                    return first_count_list_odd


            print(first_count(numbers))

    elif "last" in command:
        if list_command[2] == "even" or list_command[2] == "odd":
            def last_count(numbers):
                if int(list_command[1]) > len(numbers):
                    return "Invalid count"
                last_count_list_even = []
                last_count_list_odd = []
                for ind, last_counts in enumerate(reversed(numbers), 0):
                    if list_command[2] == "even":
                        if len(last_count_list_even) == int(list_command[1]):
                            break
                        if int(last_counts) % 2 == 0:
                            last_count_list_even.insert(0, (int(last_counts)))
                    else:
                        if len(last_count_list_odd) == int(list_command[1]):
                            break
                        if int(last_counts) % 2 != 0:
                            last_count_list_odd.insert(0, (int(last_counts)))
                if list_command[2] == "even":
                    return last_count_list_even
                else:
                    return last_count_list_odd
            print(last_count(numbers))
int_list = [int(i) for i in numbers]
print(int_list)
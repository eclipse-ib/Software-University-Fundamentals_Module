books_shelf = input().split("&")

while True:
    commands = input().split(" | ")
    if "Done" in commands[0]:
        print(', '.join(books_shelf))
        break

    command, __ = commands[0].split()

    if "Add" == command:
        add_book_name = commands[1]
        if add_book_name in books_shelf:
            continue
        else:
            books_shelf.insert(0, add_book_name)

    elif "Take" == command:
        take_book_name = commands[1]
        if take_book_name in books_shelf:
            books_shelf.remove(take_book_name)
        else:
            continue

    elif "Swap" == command:
        book_1 = commands[1]
        book_2 = commands[2]
        if book_1 in books_shelf and book_2 in books_shelf:
            book_1_index = books_shelf.index(book_1)
            book_2_index = books_shelf.index(book_2)
            books_shelf[book_1_index], books_shelf[book_2_index] = books_shelf[book_2_index],\
            books_shelf[book_1_index]

    elif "Insert" == command:
        insert_book_name = commands[1]
        books_shelf.append(insert_book_name)

    elif "Check" == command:
        check_index = int(commands[1])
        if check_index < 0 or check_index > len(books_shelf)-1:
            continue
        else:
            print(f"{books_shelf[check_index]}")


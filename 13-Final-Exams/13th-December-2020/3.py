data = input()
sent_mails = {}
while data != 'Statistics':
    new_data = data.split('->')
    command = new_data[0]
    user = new_data[1]
    if len(new_data) > 2:
        message = new_data[2]
    # add user
    if command == 'Add':
        if user not in sent_mails:
            sent_mails[user] = []
        elif user in sent_mails:
            print(f'{user} is already registered')
    elif command == 'Send':
        if user not in sent_mails:
            data = input()
            continue
        else:
            sent_mails[user].append(message)
    elif command == 'Delete':
        if user not in sent_mails:
            print(f'{user} not found!')
        else:
            sent_mails.pop(user)
    data = input()

if len(sent_mails.keys()) == 0:
    print(f'Users count: 0')
    quit()
print(f'Users count: {len(sent_mails.keys())}')

sorted_sent_mails = dict(sorted(sent_mails.items(), key=lambda x: (-len(x[1]), x[0])))

for name, message in sorted_sent_mails.items():
    print(f'{name}')
    for messe in message:
        print(f' - {messe}')


# Второ мое решение
class Party:
    def __init__(self):
        self.people = []

    def invite_guests(self):
        self.people.append(command)

    def list_of_guests(self):
        return ', '.join(self.people)

    def lenght_of_guests(self):
        return len(self.people)

    def print_results(self):
        return f"Going: {party.list_of_guests()}\nTotal: {party.lenght_of_guests()}"


party = Party()

while True:
    command = input()
    if command == "End":
        break
    party.invite_guests()

# print(f"Going: {party.list_of_guests()}")
# print(f"Total: {party.lenght_of_guests()}")
print(party.print_results())



# Първо мое решение
# class Party:
#     def __init__(self):
#         self.people = []
#
# party = Party()
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     party.people.append(command)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")




# Най-оптималния вариант с използването на 2 класа :
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Party:
#     def __init__(self):
#         self.people = []
#
#     def invite(self, person):
#         self.people.append(person)
#
#     def names_of_people(self):
#         return ", ".join([person.name for person in self.people])
#
#     def number_of_people(self):
#         return len(self.people)
#
#
# party = Party()
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     name = command
#     person = Person(name)
#     party.invite(person)
#
# print(f"Going: {party.names_of_people()}")
# print(f"Total: {party.number_of_people()}")


# # Работещ вариант само с един клас:
# class Party:
#     def __init__(self):
#         self.people = []
#
#     def invite(self, person):
#         self.people.append(person)
#
#     def names_of_people(self):
#         return ", ".join([person for person in self.people])
#
#     def number_of_people(self):
#         return len(self.people)
#
#
# party = Party()
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     name = command
#     party.invite(name)
#
# print(f"Going: {party.names_of_people()}")
# print(f"Total: {party.number_of_people()}")


# От презентацията:
# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
#
# while True:
#     line = input()
#     if line == "End":
#         break
#     party.people.append(line)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

import re

inputs = int(input())

regex = r"[U$]+([A-Z]{1}[a-z]{2,})[U$]+[P@$]+([A-Za-z]{5,}\d+)[P@$]+"

successful_reg = 0

for reg in range(inputs):
    registration = input()
    is_it_regex = re.findall(regex, registration)
    if is_it_regex:
        print(f"Registration was successful\n"
              f"Username: {is_it_regex[0][0]}, Password: {is_it_regex[0][1]}"
              )
        successful_reg += 1
    else:
        print(f"Invalid username or password")
print(f"Successful registrations: {successful_reg}")
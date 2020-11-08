import re

regex = r"([#|$|%|*|&])(?P<rider>[A-z]+)(\1)=(?P<geohashcode>\d+)!!(?P<encrypted_code>.+)"

while True:
    message = input()
    if re.search(regex, message) is None:
        print(f"Nothing found!")
        continue
    valid_message = re.finditer(regex, message, re.MULTILINE)
    if valid_message:
        for match in valid_message:
            geo_hash_code = int(match.group("geohashcode"))
            encrypted_code = len(match.group("encrypted_code"))
            if geo_hash_code == encrypted_code:
                decrypted_code = ""
                for i in match.group("encrypted_code"):
                    decrypted_code += chr(ord(i)+geo_hash_code)
                print(f"Coordinates found! {match.group('rider')} -> {decrypted_code}")
                exit()
            else:
                print(f"Nothing found!")



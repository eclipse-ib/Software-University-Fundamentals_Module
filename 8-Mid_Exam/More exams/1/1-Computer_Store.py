total_price_wo_taxes = 0
total_price_w_taxes = 0
total_amount_of_taxes = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        if command == "special":
            total_price_w_taxes = (total_price_wo_taxes * 1.2) * 0.9
            total_amount_of_taxes = total_price_wo_taxes * 0.2
            break
        else:
            total_price_w_taxes = total_price_wo_taxes * 1.2
            total_amount_of_taxes = total_price_wo_taxes * 0.2
            break
    if command < "0":
        print("Invalid price!")
        continue
    if type(command) == int:
        total_price_wo_taxes += int(command)
    else:
        total_price_wo_taxes += float(command)

if total_price_w_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_wo_taxes:.2f}$\n"
          f"Taxes: {total_amount_of_taxes:.2f}$\n"

          "-----------\n"
          f"Total price: {total_price_w_taxes:.2f}$")

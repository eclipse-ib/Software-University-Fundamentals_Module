# решението от лекциите --> https://www.youtube.com/watch?v=QUxIz5d5ip8&feature=youtu.be&t=33


number_of_cars = int(input())

cars = {}

for car_number in range(number_of_cars):
    new_car = input().split("|")
    car_name_dict = new_car[0]
    mileage_dict = int(new_car[1])
    fuel_dict = int(new_car[2])
    cars[car_name_dict] = (mileage_dict, fuel_dict)


while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break

    car = command[1]

    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if (cars[car])[1] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            cars[car] = ((cars[car])[0], (cars[car])[1] - fuel)
            cars[car] = ((cars[car])[0] + distance, (cars[car])[1])
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if (cars[car])[0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    elif command[0] == "Refuel":
        fuel_refuel = int(command[2])
        cars[car] = ((cars[car])[0], (cars[car])[1] + fuel_refuel)

        if (cars[car])[1] <= 75:
            print(f"{car} refueled with {fuel_refuel} liters")
        else:
            difference = fuel_refuel - ((cars[car])[1] - 75)
            print(f"{car} refueled with {difference} liters")
            cars[car] = ((cars[car])[0], 75)

    elif command[0] == "Revert":
        kilometers = int(command[2])
        cars[car] = ((cars[car])[0] - kilometers, (cars[car])[1])
        if (cars[car])[0] < 10000:
            cars[car] = ((cars[car])[0] == 10000, (cars[car])[1])
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")


for k, v in sorted(cars.items(), key=lambda item: item[1][1], reverse=True):
    print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")

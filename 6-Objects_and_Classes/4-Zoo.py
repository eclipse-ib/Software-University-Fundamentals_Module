class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, end_species):
        result = ""
        if end_species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif end_species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif end_species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


Zoo.zoo_name = input()
zoo = Zoo(Zoo.zoo_name)

for i in range(int(input())):
    species, name = input().split(' ', maxsplit=1)
    zoo.add_animal(species, name)

print(zoo.get_info(input()))
class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self._radius = diameter / 2
        self._diameter = diameter

    def calculate_circumference(self):
        return (2*Circle.__pi) * self._radius

    def calculate_area(self):
        return Circle.__pi*self._radius * self._radius

    def calculate_area_of_sector(self, angle):
        return (Circle.__pi*(self._radius**2)) * (angle/360)


circle = Circle(int(input()))

print(f"{circle.calculate_circumference():.2f}, {circle.calculate_area():.2f}, {circle.calculate_area_of_sector(int(input())):.2f}")
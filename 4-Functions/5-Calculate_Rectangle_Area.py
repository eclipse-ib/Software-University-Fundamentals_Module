def rectangle_area(width: int, height: int):
    area = width * height
    return area


width: int = int(input())
height: int = int(input())
print(f"{rectangle_area(width, height)}")
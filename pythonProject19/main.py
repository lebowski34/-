class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color if self.__is_valid_color(*color) else (0, 0, 0)
        self.filled = False
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def __is_valid_sides(self, *sides):
        return (len(sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in sides))

    def __len__(self):
        return sum(self.__sides)



import math


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi) if self.get_sides() else 1 / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_sides():
            s = sum(self.get_sides()) / 2
            self.__height = (2 / self.get_sides()[0]) * (
                        s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5
        else:
            self.__height = 1

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5



class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())
print(cube1.get_volume())

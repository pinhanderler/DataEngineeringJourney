class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def calculate_area(self):
        return self.width ** 2


if __name__ == "__main__":
    rect = Rectangle(5, 8)
    square = Square(6, 6)
    print("Rectangle Area:", rect.calculate_area())
    print("Square Area:", square.calculate_area())

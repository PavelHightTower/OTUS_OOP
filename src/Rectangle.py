from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        super().__init__(side_a, side_a)


s = Square(3)

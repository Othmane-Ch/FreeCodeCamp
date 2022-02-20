class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for _ in range(self.height):
            picture += f"{'*' * self.width}\n"
        return picture

    def get_amount_inside(self, shape) -> int:
        h = self.height // shape.height
        w = self.width // shape.width
        return h * w

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def set_side(self, side) -> None:
        Rectangle.set_height(self, side)
        Rectangle.set_width(self, side)

    def __str__(self):
        return f"Square(side={self.width})"

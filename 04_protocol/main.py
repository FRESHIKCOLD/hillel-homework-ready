from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> str:
        ...


def render(shape: Drawable) -> None:
    print(shape.draw())


class Circle:
    def draw(self) -> str:
        return "( )"


class Square:
    def draw(self) -> str:
        return "[ ]"


if __name__ == "__main__":
    render(Circle())
    render(Square())

import os
import random
from dataclasses import dataclass

from src import settings
from src.term_seq import move_to_top_of_the_screen, clear_line, move_down


@dataclass(slots=True, frozen=True)
class Position:
    col: int = 0
    row: int = 0

    def __repr__(self) -> str:
        return f"Position({self.col}, {self.row})"


@dataclass
class Boundary:
    bound1: Position
    bound2: Position

    def __contains__(self, item: Position) -> bool:
        if not isinstance(item, Position):
            return False

        return (
            self.bound1.row <= item.row <= self.bound2.row and
            self.bound1.col <= item.col <= self.bound2.col
        ) or (
            self.bound2.row <= item.row <= self.bound1.row and
            self.bound2.col <= item.col <= self.bound1.col
        )

    def __repr__(self) -> str:
        return f"Boundary({self.bound1}, {self.bound2})"


def get_random_position_in_boundary(boundary: Boundary) -> Position:
    b1 = boundary.bound1
    b2 = boundary.bound2

    col = random.randint(b1.col, b2.col)
    row = random.randint(b1.row, b2.row)

    return Position(col=col, row=row)


def get_screen_boundary() -> Boundary:
    term_size = os.get_terminal_size()
    return Boundary(
        Position(col=0, row=0),
        Position(col=term_size.columns, row=term_size.lines),
    )


def clear_screen() -> None:
    term_size = os.get_terminal_size()
    move_to_top_of_the_screen()

    for _ in range(term_size.lines):
        clear_line()
        move_down()


def reverse_median(
        val: int,
        left: int = settings.MIN_WORD_SPEED,
        right: int = settings.MAX_WORD_SPEED,
) -> int:
    """
    Возвращает зеркальное значение относительно медианы диапазона
    """
    return right - val + left

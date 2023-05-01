from __future__ import annotations

from src import settings
from src.utils import Position


class Symbol:
    def __init__(
            self,
            char: str = '',
            position: Position | None = None,
            color: int = settings.COLORS[0],
            is_visible: bool = True,
    ) -> None:
        self._char = char
        self._position = isinstance(position, Position) and position or Position(0, 0)
        self._color = color
        self._is_visible = is_visible

    def set_next_color(self) -> None:
        if self.has_last_color():
            return
        self._color = settings.COLORS[settings.COLORS.index(self._color) + 1]

    def has_last_color(self) -> bool:
        return self._color == settings.COLORS[-1]

    def __eq__(self, other: Symbol) -> bool:
        return (
            self._char == other.char and
            self._position == other.position and
            self._color == other.color
        )

    @property
    def char(self) -> str:
        return self._char

    @property
    def position(self) -> Position:
        return self._position

    @property
    def color(self) -> int:
        return self._color

    @property
    def is_visible(self) -> bool:
        return self._is_visible

    @is_visible.setter
    def is_visible(self, val: bool) -> None:
        self._is_visible = val

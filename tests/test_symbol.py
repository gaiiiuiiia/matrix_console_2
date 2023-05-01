from src import settings
from src.symbol import Symbol
from src.utils import Position


def test_symbol_defaults() -> None:
    symbol = Symbol()

    assert symbol.char is ''
    assert symbol.position == Position(col=0, row=0)
    assert symbol.color == settings.COLORS[0]
    assert symbol.is_visible


def test_symbol_set_next_color() -> None:
    symbol = Symbol()
    current_color = symbol.color

    symbol.set_next_color()

    assert settings.COLORS[settings.COLORS.index(current_color) + 1] == symbol.color


def test_symbol_set_next_color_when_last_color() -> None:
    symbol = Symbol(color=settings.COLORS[-1])
    current_color = symbol.color

    symbol.set_next_color()

    assert symbol.color == current_color

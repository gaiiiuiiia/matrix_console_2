import random

import pytest

from src import settings
from src.enums import Direction
from src.symbol import Symbol
from src.utils import Boundary, Position
from src.word import Word, get_random_word


@pytest.fixture
def dictionary() -> list[str]:
    return [f"word_{i}" for i in range(10)]


def test_word_defaults() -> None:
    word = Word('some')

    assert word.value == 'some'
    assert word.position == Position(0, 0)
    assert word.direction == Direction.DOWN
    assert word.speed == 1


def test_word_max_speed() -> None:
    word = Word('some', speed=settings.MAX_WORD_SPEED + 1)

    assert word.speed == settings.MAX_WORD_SPEED


def test_word_min_speed() -> None:
    word = Word('some', speed=settings.MIN_WORD_SPEED - 1)

    assert word.speed == settings.MIN_WORD_SPEED


def test_word_speed() -> None:
    speed = random.randint(settings.MIN_WORD_SPEED, settings.MAX_WORD_SPEED)
    word = Word('some', speed=speed)

    assert word.speed == speed


def test_word_symbols() -> None:
    word = Word('some')

    assert word.symbols == (
        Symbol('s', Position(0, 0)),
        Symbol('o', Position(0, 1)),
        Symbol('m', Position(0, 2)),
        Symbol('e', Position(0, 3)),
    )


def test_can_iterate_over_word() -> None:
    word = Word('some')
    assert word.symbols == tuple(symbol for symbol in word)


def test_word_get_offset_position_up() -> None:
    position = Position(0, 0)
    word = Word('some', position, Direction.UP)

    for i in range(len(word.value)):
        assert word._get_offset_position(i) == Position(position.col, position.row - i)


def test_word_get_offset_position_right() -> None:
    position = Position(0, 0)
    word = Word('some', position, Direction.RIGHT)

    for i in range(len(word.value)):
        assert word._get_offset_position(i) == Position(position.col + i, position.row)


def test_word_get_offset_position_down() -> None:
    position = Position(0, 0)
    word = Word('some', position, Direction.DOWN)

    for i in range(len(word.value)):
        assert word._get_offset_position(i) == Position(position.col, position.row + i)


def test_word_get_offset_position_left() -> None:
    position = Position(0, 0)
    word = Word('some', position, Direction.LEFT)

    for i in range(len(word.value)):
        assert word._get_offset_position(i) == Position(position.col - i, position.row)


def test_get_random_word(dictionary) -> None:
    boundary = Boundary(Position(0, 0), Position(10, 10))
    word = get_random_word(
        dictionary=dictionary,
        boundary=boundary,
        direction=Direction.DOWN,
    )

    assert word.value in dictionary
    assert word.position in boundary
    assert word.direction == Direction.DOWN

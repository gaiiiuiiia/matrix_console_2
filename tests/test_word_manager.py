from typing import Generator

import pytest as pytest

from src.enums import Direction
from src.utils import Position, Boundary
from src.word import word_generator, Word
from src.word_manager import WordManager


@pytest.fixture(scope="module")
def max_words() -> int:
    return 20


@pytest.fixture(scope="module")
def dictionary() -> list[str]:
    return ['some', 'day', 'unique']


@pytest.fixture(scope="module")
def boundary() -> Boundary:
    return Boundary(Position(0, 0), Position(10, 10))


@pytest.fixture(scope="module", name="word_generator")
def word_generator_fixture(dictionary, boundary) -> Generator[Word, None, None]:
    return word_generator(dictionary, boundary, Direction.DOWN)


@pytest.fixture
def word_manager(max_words, word_generator) -> WordManager:
    return WordManager(word_generator, max_words)


def test_word_manager_words(word_manager, dictionary, boundary) -> None:
    assert len(word_manager.words) == word_manager.max_words

    for word in word_manager.words:
        assert isinstance(word, Word)
        assert word.value in dictionary
        assert word.position in boundary

from dataclasses import dataclass

from src.utils import reverse_median
from src.word import Word


def _is_tick_frame(current_frame: int, speed: int) -> bool:
    return current_frame % reverse_median(speed) == 0


@dataclass
class WordInfo:
    current_symbol_index: int = 0


class WordManager:
    def __init__(self, word_generator, max_words: int = 0) -> None:
        self._word_generator = word_generator
        self._max_words = max_words >= 0 and max_words or 0
        self._words_info = self._initialize_words(self._max_words)

    def tick(self, frame: int) -> None:
        for i, (word, word_info) in enumerate(self._words_info.items()):
            if not _is_tick_frame(frame, word.speed):
                continue

            if word_info.current_symbol_index < len(word.value):
                word[word_info.current_symbol_index].is_visible = True
                word_info.current_symbol_index += 1

            for symbol in word[:word_info.current_symbol_index]:
                if not symbol.has_last_color():
                    symbol.set_next_color()
                else:
                    symbol.is_visible = False

        if count := self._remove_draw_words():
            self._prepare_new_words(count)

    def _initialize_words(self, count: int) -> dict[Word: WordInfo]:
        words_info = {
            next(self._word_generator): WordInfo()
            for _ in range(count)
        }

        for word in words_info.keys():
            for symbol in word:
                symbol.is_visible = False

        return words_info

    def _remove_draw_words(self) -> int:
        words_to_remove = [
            word for (word, word_info) in self._words_info.items()
            if all(not symbol.is_visible for symbol in word)
            and word_info.current_symbol_index == len(word.value)
        ]

        removed_words_count = len(words_to_remove)
        for word in words_to_remove:
            self._words_info.pop(word)

        return removed_words_count

    def _prepare_new_words(self, count: int) -> None:
        if len(self._words_info) == self._max_words:
            return

        count = min(count, self._max_words - len(self._words_info))
        new_words = self._initialize_words(count)
        self._words_info.update(new_words)

    @property
    def words(self):
        return self._words_info.keys()

    @property
    def max_words(self) -> int:
        return self._max_words

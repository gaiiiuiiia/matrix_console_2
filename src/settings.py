import random


def _generate_dictionary(
        alphabet: list[str],
        count: int,
        min_len: int,
        max_len: int,
) -> list[str]:
    dictionary: list[str] = []
    for _ in range(count):
        word_len = random.randint(min_len, max_len)
        symbols = [random.choice(alphabet) for _ in range(word_len)]
        dictionary.append("".join(symbols))

    return dictionary


FPS = 40
MAX_WORDS_ON_SCREEN = 80
MIN_WORD_SPEED = 1
MAX_WORD_SPEED = 5
MIN_WORD_LEN = 8
MAX_WORD_LEN = 16


# палитра цветов от зеленого к черному
COLORS = (155, 154, 46, 40, 34, 28, 22, 0)

ALPHABET = [chr(int("0x30a0", 16) + i) for i in range(96)]
DICTIONARY = _generate_dictionary(ALPHABET, MAX_WORDS_ON_SCREEN, MIN_WORD_LEN, MAX_WORD_LEN)

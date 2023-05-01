import os
import sys
import time
import tty
from typing import Callable

from src.render import render_words
from src.settings import (
    DICTIONARY, MAX_WORDS_ON_SCREEN, FPS
)
from src.term_seq import make_cursor_visible
from src.utils import get_screen_boundary
from src.word import word_generator
from src.word_manager import WordManager


def main() -> None:
    tty.setcbreak(sys.stdin)
    os.system('clear')
    make_cursor_visible(False)

    boundary = get_screen_boundary()
    generator = word_generator(DICTIONARY, boundary)
    word_manager = WordManager(generator, MAX_WORDS_ON_SCREEN)

    def mainloop_callback(frame: int) -> None:
        render_words(word_manager.words)
        word_manager.tick(frame)

    mainloop(mainloop_callback)
    make_cursor_visible()


def mainloop(callback: Callable[[int], None]) -> None:
    current_frame = 1
    try:
        while True:
            t1 = time.time()
            callback(current_frame)
            delta = time.time() - t1

            if (sleep_time := 1 / FPS - delta) > 0:
                time.sleep(sleep_time)
            current_frame += 1
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

from src.term_seq import (
    move_to_bottom,
    save_cursor_position,
    move_to,
    set_foreground_color,
    restore_cursor_position,
    write,
)
from src.utils import clear_screen
from src.word import Word


def render_words(words: list[Word]) -> None:
    move_to_bottom()
    save_cursor_position()
    clear_screen()

    for word in words:
        for symbol in word:
            if symbol.is_visible:
                move_to(symbol.position.row, symbol.position.col)
                set_foreground_color(symbol.color)
                write(symbol.char)

    restore_cursor_position()

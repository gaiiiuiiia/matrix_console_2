import os
import sys
from typing import Any

"""
https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
"""

ESC = "\033"


def escape_write(command: Any) -> None:
    sys.stdout.write(ESC + str(command))


def write(text: str) -> None:
    sys.stdout.write(text)
    sys.stdout.flush()


def make_cursor_visible(is_visible: bool = True) -> None:
    if is_visible:
        return escape_write("[?25h")
    return escape_write("[?25l")


def set_background_color(color_id: int) -> None:
    escape_write(f"[48;5;{color_id}m")


def set_foreground_color(color_id: int) -> None:
    escape_write(f"[38;5;{color_id}m")


def save_cursor_position() -> None:
    escape_write(7)


def restore_cursor_position() -> None:
    escape_write(8)


def move_to_top_of_the_screen() -> None:
    escape_write("[H")


def delete_line() -> None:
    escape_write("[2K")


def clear_line() -> None:
    delete_line()
    move_to_col()


def move_to_col(col: int = 0) -> None:
    escape_write(f"[{col}G")


def move_to_row(row: int = 0) -> None:
    # moves to zero col of given row
    escape_write(f"[{row};0H")


def move_left(count: int = 1) -> None:
    escape_write(f"[{count}D")


def move_right(count: int = 1) -> None:
    escape_write(f"[{count}C")


def move_down(rows: int = 1) -> None:
    escape_write(f"[{rows}B")


def move_up(rows: int = 1) -> None:
    escape_write(f"[{rows}A")


def move_to_bottom() -> None:
    term_size = os.get_terminal_size()
    escape_write(f"[{term_size.lines - 1}E")


def move_to(row: int, col: int) -> None:
    move_to_row(row)
    move_to_col(col)

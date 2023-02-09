import curses
from curses import wrapper


def main(stdscr):
    # adding colours to the terminal
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    WHITE_AND_BLUE = curses.color_pair(1)

    stdscr.clear()
    stdscr.addstr(10, 10, "Hello, World!", WHITE_AND_BLUE | curses.A_BLINK)
    stdscr.addstr(15, 20, "How are you, World?", WHITE_AND_BLUE | curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)

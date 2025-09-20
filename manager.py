import curses
import sys
from ui.download import download_menu
from ui.run import run_menu

MENU_OPTIONS = [
    "Download Scratch",
    "Run Scratch",
    "Exit"
]

def main_menu(stdscr):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, option in enumerate(MENU_OPTIONS):
            x = w//2 - len(option)//2
            y = h//2 - len(MENU_OPTIONS)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, option)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(MENU_OPTIONS) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, ord('\n')]:
            if current_row == 0:  # Download Scratch
                download_menu(stdscr)
            elif current_row == 1:  # Run Scratch
                run_menu(stdscr)
            elif current_row == 2:  # Exit
                break

def run():
    curses.wrapper(init_curses)

def init_curses(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    main_menu(stdscr)

if __name__ == "__main__":
    run()
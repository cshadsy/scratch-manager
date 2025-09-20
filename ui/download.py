import curses
import os
import subprocess

DOWNLOAD_OPTIONS = [
    "Scratch 3.0 (scratch-gui)",
    "Scratch 3.0 (scratch-editor)",
    "TurboWarp",
    "PenguinMod",
    "PenguinMod (Devel)"
]

def clone_scratch_gui(stdscr):
    install_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "installations", "scratch-gui")
    if os.path.exists(install_dir):
        msg = "scratch-gui already exists!"
    else:
        stdscr.clear()
        stdscr.addstr(0, 0, "Cloning scratch-gui...\n")
        stdscr.refresh()
        try:
            subprocess.run(["git", "clone", "https://github.com/scratchfoundation/scratch-gui.git", install_dir], check=True)
            stdscr.addstr(1, 0, "Running npm install --force...\n")
            stdscr.refresh()
            subprocess.run(["npm", "install", "--force"], cwd=install_dir, check=True)
            msg = "scratch-gui downloaded and dependencies installed!"
        except Exception as e:
            msg = f"Error: {e}"
    stdscr.clear()
    stdscr.addstr(0, 0, msg)
    stdscr.addstr(2, 0, "Press any key to return.")
    stdscr.refresh()
    stdscr.getch()

def download_menu(stdscr):
    curses.curs_set(0)
    current_row = 0
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, option in enumerate(DOWNLOAD_OPTIONS):
            x = w//2 - len(option)//2
            y = h//2 - len(DOWNLOAD_OPTIONS)//2 + idx
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
        elif key == curses.KEY_DOWN and current_row < len(DOWNLOAD_OPTIONS) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, ord('\n')]:
            if current_row == 0:
                clone_scratch_gui(stdscr)
            # other options do nothing for now
        elif key == 27:  # escape to exit submenu
            break
    curses.curs_set(0)
    current_row = 0
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, option in enumerate(DOWNLOAD_OPTIONS):
            x = w//2 - len(option)//2
            y = h//2 - len(DOWNLOAD_OPTIONS)//2 + idx
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
        elif key == curses.KEY_DOWN and current_row < len(DOWNLOAD_OPTIONS) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, ord('\n')]:
            if current_row == 0:
                clone_scratch_gui(stdscr)
            # other options do nothing for now
        elif key == 27:  # escape to exit submenu
            break

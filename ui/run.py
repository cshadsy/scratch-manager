import curses
import os
import subprocess

INSTALLATIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "installations")

def get_installations():
    if not os.path.exists(INSTALLATIONS_DIR):
        return []
    return [d for d in os.listdir(INSTALLATIONS_DIR) if os.path.isdir(os.path.join(INSTALLATIONS_DIR, d))]

def run_installation(stdscr, folder):
    install_path = os.path.join(INSTALLATIONS_DIR, folder)
    stdscr.clear()
    stdscr.addstr(0, 0, f"Building {folder}...\n")
    stdscr.refresh()
    try:
        subprocess.run(["npm", "run", "build"], cwd=install_path, check=True)
        stdscr.addstr(1, 0, f"Starting {folder}...\n")
        stdscr.refresh()
        subprocess.run(["npm", "run", "start"], cwd=install_path, check=True)
        msg = f"{folder} started successfully!"
    except Exception as e:
        msg = f"Error: {e}"
    stdscr.clear()
    stdscr.addstr(0, 0, msg)
    stdscr.addstr(2, 0, "Press any key to return.")
    stdscr.refresh()
    stdscr.getch()

def run_menu(stdscr):
    curses.curs_set(0)
    installations = get_installations()
    if not installations:
        stdscr.addstr(0, 0, "No installations found.")
        stdscr.addstr(2, 0, "Press any key to return.")
        stdscr.refresh()
        stdscr.getch()
        return
    current_row = 0
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, folder in enumerate(installations):
            x = w//2 - len(folder)//2
            y = h//2 - len(installations)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, folder)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, folder)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(installations) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, ord('\n')]:
            run_installation(stdscr, installations[current_row])
        elif key == 27:  # escape to exit submenu
            break

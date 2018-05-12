import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

while True:
    c = stdscr.getch()
    stdscr.refresh()
    stdscr.addstr(0,0, str(c) + ' => ' +chr(c))
    if c == curses.KEY_LEFT:
        stdscr.addstr(0,0,'Gauche  ')
    elif c == curses.KEY_RIGHT:
        stdscr.addstr(0,0,'Droite  ')
    elif c == curses.KEY_UP:
        stdscr.addstr(0,0,'Monte  ')
    elif c == curses.KEY_DOWN:
        stdscr.addstr(0,0,'Descend  ')
    elif c == 27:
        stdscr.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        break

print("bye")

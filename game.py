import curses, os

from news.news import load_graphic

def quit(stdscr):
    """Return terminal settings to normal"""
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

def main():
    """Main game loop"""
    stdscr = curses.initscr()
    # TODO: add title
    curses.noecho()
    # initialize curses color
    curses.start_color()
    # TODO: initialize array of color pairs?
    # turn off cursor
    curses.curs_set(0)
    # begin game loop
    stdscr.keypad(1)
    curses.raw()
    bigletters, newstops, newspic = (load_graphic(os.path.join('art', fn)) for fn in ('largecap.cpc', 'newstops.cpc', 'newspic.cpc'))

    # quit game
    quit(stdscr)

if __name__ == '__main__': main()

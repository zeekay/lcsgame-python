import os

def readConfigFile(fn, stdscr):
    """Reads configuration file"""
    stdscr.addstr('Attempting to open filename: ')
    stdscr.addstr(fn)
    stdscr.addstr(' ')

    objects = []
    object = {}

    with open(os.path.join('art', fn)) as f:
        while True:
            line = f.readline()
            if not line:
                objects.append(object)
                break
            command, value = line.strip().split()
            if command == 'OBJECT':
                objects.append(object)
                object = {'type': value}
            else:
                object[command] = value

    return objects

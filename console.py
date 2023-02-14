#!/usr/bin/python3

"""command line commands for creating, quitting,
help, destroying, showing, updating, 
all, update
"""

from cmd import Cmd


class HBNBCommand(Cmd):
    """Class for console commands
    """
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
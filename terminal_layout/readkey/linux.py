# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
import sys
import tty
import termios

from terminal_layout.readkey.key import Key


def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def readkey():
    c1 = getchar()
    if ord(c1) != 0x1b:
        if c1 == Key.CTRL_C:
            raise KeyboardInterrupt
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1 + c2
    c3 = getchar()
    if ord(c3) != 0x33:
        return c1 + c2 + c3
    c4 = getchar()
    return c1 + c2 + c3 + c4

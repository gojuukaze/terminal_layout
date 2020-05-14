# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt
import sys

from terminal_layout.readkey.key import Key

mapping = {
    13: Key.ENTER,
    27: Key.ESC,

    18656: Key.UP,
    20704: Key.DOWN,
    19424: Key.LEFT,
    19936: Key.RIGHT,
    b'\x08': Key.BACKSPACE
}


def readkey():
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            a = ord(ch)
            if a == 0 or a == 224:
                b = ord(msvcrt.getch())
                x = a + (b * 256)
                try:
                    return mapping[x]
                except KeyError:
                    return None
            else:
                return ch.decode()

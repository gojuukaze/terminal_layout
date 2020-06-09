# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/#c9
# Thanks to Stephen Chappell
import msvcrt

from terminal_layout.readkey.key import Key
from terminal_layout.logger import logger

xlate_dict = {
    8: Key.BACKSPACE.code,
    13: Key.ENTER.code,
    27: Key.ESC.code,
    15104: Key.F1.code,
    15360: Key.F2.code,
    15616: Key.F3.code,
    15872: Key.F4.code,
    16128: Key.F5.code,
    16384: Key.F6.code,
    16640: Key.F7.code,
    16896: Key.F8.code,

    18656: Key.UP.code,
    20704: Key.DOWN.code,
    19424: Key.LEFT.code,
    19936: Key.RIGHT.code,
}


def readkey():
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            a = ord(ch)
            if a == 0 or a == 224:
                b = ord(msvcrt.getch())
                x = a + (b * 256)
                return xlate_dict.get(x, None)
            else:
                return xlate_dict.get(a, ch.decode())

# -*- coding: utf-8 -*-

import subprocess
try:
    from os import get_terminal_size
except:
    from backports.shutil_get_terminal_size import get_terminal_size


def get_terminal_size2():
    """
    之前写的，暂时不用了
    """
    r = subprocess.check_output("stty size", shell=True)
    try:
        size = str(r, encoding="utf8").strip().split(' ')
    except:
        # py2
        size = str(r).strip().split(' ')
    return int(size[0]), int(size[1])


def is_ascii(c):
    return 255 >= ord(c) >= 0

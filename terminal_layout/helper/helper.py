# -*- coding: utf-8 -*-

import subprocess


def get_terminal_size():
    """
    Returns the size of the terminal

    Args:
    """
    r = subprocess.check_output("stty size", shell=True)
    try:
        size = str(r, encoding="utf8").strip().split(' ')
    except:
        # py2
        size = str(r).strip().split(' ')
    return int(size[0]), int(size[1])


def is_ascii(c):
    """
    Return true if c is an ascii ascii string.

    Args:
        c: (array): write your description
    """
    return 255 >= ord(c) >= 0

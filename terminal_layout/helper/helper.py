# -*- coding: utf-8 -*-

import subprocess


def get_terminal_size():
    r = subprocess.check_output("stty size", shell=True)
    try:
        size = str(r, encoding="utf8").strip().split(' ')
    except:
        # py2
        size = str(r).strip().split(' ')
    return int(size[0]), int(size[1])


def is_ascii(c):
    return 255 >= ord(c) >= 0

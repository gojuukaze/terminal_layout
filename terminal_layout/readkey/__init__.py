"""
based on https://github.com/magmax/python-readchar

support python 3+
"""
import sys

if sys.version_info >= (3, 0):
    from terminal_layout.readkey.key import Key
    from terminal_layout.readkey.listener import KeyListener

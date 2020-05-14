"""
based on https://github.com/magmax/python-readchar
"""
import sys

if sys.platform in ('win32', 'cygwin'):
    from terminal_layout.readkey.windows import readkey
else:
    from terminal_layout.readkey.linux import readkey


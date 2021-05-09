"""
input初期的测试代码，放到这只做备忘
"""

import sys
from terminal_layout import KeyListener, Key
import logging

from terminal_layout.types import String

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
handler = logging.FileHandler("terminal_layout.log")
logger.addHandler(handler)

from terminal_layout.ansi import Cursor


k = KeyListener()

s = String('')
s_char_list_index = 0
cursor_index = 0


@k.bind_key('any')
def _(_, e):
    global s, s_char_list_index, cursor_index

    c = e.key.code
    logger.debug(f's={s},  c={c}')

    if repr(c).startswith("'\\x") or repr(c).startswith("u'\\x"):

        if e.key == Key.LEFT and s_char_list_index > 0:
            back = len(s.char_list[s_char_list_index - 1])
            cursor_index -= back
            s_char_list_index -= 1
            sys.stdout.write(Cursor.BACK(back))

        if e.key == Key.RIGHT and s_char_list_index < len(s.char_list):
            forward = len(s.char_list[s_char_list_index])
            cursor_index += forward
            s_char_list_index += 1
            sys.stdout.write(Cursor.FORWARD(forward))

        if e.key == Key.BACKSPACE and s_char_list_index > 0:
            back = len(s.char_list[s_char_list_index - 1])
            cursor_index -= back
            s_char_list_index -= 1

            len_right_s = 0
            show_s = ''
            for c in s.get_char_list_item(s_char_list_index + 1):
                len_right_s += len(c)
                show_s += str(c)

            s.pop(s_char_list_index)

            logger.info(f'{back} - {len_right_s} - {show_s} - {repr(Cursor.BACK(len_right_s) if len_right_s else "")}')

            sys.stdout.write(
                Cursor.BACK(back) + ' ' * (len_right_s + back) + Cursor.BACK(len_right_s + back) + show_s)

            if len_right_s > 0:
                sys.stdout.write(Cursor.BACK(len_right_s))


    else:
        show_s = c
        c_str = String(c)
        after_show_s = ''
        len_right_s = 0
        for c in s.get_char_list_item(s_char_list_index):
            len_right_s += len(c)
            show_s += str(c)

        if len_right_s > 0:
            sys.stdout.write(' ' * len_right_s + Cursor.BACK(len_right_s))
            after_show_s = Cursor.BACK(len_right_s)

        sys.stdout.write(show_s + after_show_s)

        s.insert_into_char_list(s_char_list_index, c_str)
        s_char_list_index += len(c_str.char_list)
        cursor_index += len(c_str)
        logger.debug(f's_char_list_index={s_char_list_index}, cursor_index={cursor_index}, s={s}')

    sys.stdout.flush()


s1 = 'bbb, input:'
sys.stdout.write(s1)
sys.stdout.write('\n')
sys.stdout.write('asd222\n' + Cursor.UP(2) + Cursor.FORWARD(len(s1)))
sys.stdout.flush()
k.listen(stop_key=[Key.ENTER])

print('\nasd222')

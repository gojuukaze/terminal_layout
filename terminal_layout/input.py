"""
inputView两种实现方法：
1. 外部监听key事件，然后通过 setText 修改已有的textView值。这样做需要自己移动光标，频繁的redraw
2. 基于textView写个view，这样做需要在view内自己处理 宽度，以及父view 相关的逻辑问题

目前使用第一种
"""
import sys

from terminal_layout.view.params import Visibility

from terminal_layout.ansi import Cursor
from terminal_layout.readkey import Key, KeyListener
from terminal_layout.types import String


class InputPlus(object):

    def __init__(self, ctl):
        self.ctl = ctl

    def get_view_x_y(self, id):
        """

        (x, y)--------------
        |   1     2     3   |
        |   4     5     6   |
        |   7     8     9   |
        --------------(x, y)

        (1,2) = 6
        """
        x = 0
        y = 0
        for row in self.ctl.layout.data:
            if row.visibility == Visibility.gone:
                continue
            if row.visibility == Visibility.visible:
                for v in row.data:
                    if v.id == id:
                        if v.visibility != Visibility.visible:
                            return -1, -1
                        return x, y
                    y += v.real_width or 0
            x += 1
            y = 0

    def get_input(self, id):
        self.view = self.ctl.find_view_by_id(id)
        if not self.view:
            return False, ''
        self.x, self.y = self.get_view_x_y(id)
        if self.x < 0 or self.y < 0:
            return False, ''

        self.layout_height = self.ctl.layout.real_height

        self.s = String(self.view.get_text())
        self.s_char_list_index = len(self.s.char_list)
        self.cursor_index = len(self.s)

        self.move_cursor_to_view()
        kl = KeyListener()

        kl.bind_key('any', self.key_event, decorator=False)

        kl.listen()
        self.move_cursor_to_btm()
        return str(self.s)

    def move_cursor_to_view(self):
        s = ''
        if self.layout_height - self.x > 0:
            s += Cursor.UP(self.layout_height - self.x)
        if self.y + self.cursor_index > 0:
            s += Cursor.FORWARD(self.y + self.cursor_index)
        if s:
            sys.stdout.write(s)
            sys.stdout.flush()

    def move_cursor_to_btm(self):
        s = ''
        if self.layout_height - self.x > 0:
            s += Cursor.DOWN(self.layout_height - self.x)
        if self.y + self.cursor_index > 0:
            s += Cursor.BACK(self.y + self.cursor_index)
        if s:
            sys.stdout.write(s)
            sys.stdout.flush()

    def update_text(self):

        self.view.set_text(str(self.s))
        self.ctl.re_draw()
        self.move_cursor_to_view()

    def key_event(self, kl, event):
        c = event.key.code

        if len(repr(c))>1 and (repr(c).startswith("'\\") or repr(c).startswith("u'\\")):
            if event.key == Key.LEFT and self.s_char_list_index > 0:
                back = len(self.s.char_list[self.s_char_list_index - 1])
                self.cursor_index -= back
                self.s_char_list_index -= 1
                sys.stdout.write(Cursor.BACK(back))
                sys.stdout.flush()

            elif event.key == Key.RIGHT and self.s_char_list_index < len(self.s.char_list):
                forward = len(self.s.char_list[self.s_char_list_index])
                self.cursor_index += forward
                self.s_char_list_index += 1
                sys.stdout.write(Cursor.FORWARD(forward))
                sys.stdout.flush()

            elif event.key == Key.BACKSPACE and self.s_char_list_index > 0:
                self.move_cursor_to_btm()
                back = len(self.s.char_list[self.s_char_list_index - 1])
                self.cursor_index -= back
                self.s_char_list_index -= 1
                self.s.pop(self.s_char_list_index)
                self.update_text()
            elif event.key == Key.ENTER:
                kl.stop()
        else:
            self.move_cursor_to_btm()
            c_str = String(c)

            self.s.insert_into_char_list(self.s_char_list_index, c_str)
            self.s_char_list_index += len(c_str.char_list)
            self.cursor_index += len(c_str)
            self.update_text()

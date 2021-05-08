"""
inputView两种实现方法：
1. 外部监听key事件，然后通过 setText 修改已有的textView值。这样做需要自己移动光标，频繁的redraw
2. 基于textView写个view，这样做需要在view内自己处理 宽度，以及父view 相关的逻辑问题

InputEx使用第一种
"""
import logging
import sys

from terminal_layout.log import logger
from terminal_layout.ctl import TextViewProxy, LayoutProxy

try:
    from typing import Union
except:
    pass
from terminal_layout import *

from terminal_layout.types import String


class InputEx(object):
    view = None  # type:Union[None, TextViewProxy, LayoutProxy]
    x = -1
    y = -1
    layout_height = 0
    input_s = None  # type: String
    input_char_list_index = 0
    input_char_list_start = 0
    input_char_list_end = 0
    cursor_index = 0

    def __init__(self, _ctl, input_buffer=30):
        """

        :param input_buffer: 读取字符的缓存；输入法一次输入多个字符时，若buffer过小会导致只读取到一部分

        :type _ctl:LayoutCtl
        """
        self.ctl = _ctl
        self.input_buffer = input_buffer

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
        return -1, -1

    def get_parent_max_width(self, view):
        p = view.get_parent()
        if p is None:
            return self.ctl.get_terminal_size()[0]
        else:
            parent_max_width = self.get_parent_max_width(p)
            width = p.get_width()
            if isinstance(width, int) and width < parent_max_width:
                return width
            return parent_max_width

    def get_view_max_width(self):
        parent_max_width = self.get_parent_max_width(self.view)

        parent = self.view.get_parent()
        if parent is not None:
            for v in parent.data:
                if v.id == self.view.get_id():
                    continue
                if v.weight is None:
                    parent_max_width -= v.real_width

        width = self.view.get_width()

        if isinstance(width, int) and width < parent_max_width:
            return width
        return parent_max_width

    def get_input(self, id):
        self.view = self.ctl.find_view_by_id(id)

        if not self.view or not isinstance(self.view, TextViewProxy):
            return False, ''

        self.x, self.y = self.get_view_x_y(id)
        if self.x < 0 or self.y < 0:
            return False, ''

        # 停止绘制线程
        if self.ctl.auto_re_draw:
            self.ctl.refresh_thread_stop = True
            self.ctl.refresh_thread.join()

        self.max_width = self.get_view_max_width()

        if self.max_width <= 0:
            return False, ''

        self.layout_height = self.ctl.layout.real_height

        self.input_s = String(self.view.get_text())
        self.input_char_list_index = len(self.input_s.char_list)
        self.input_char_list_start = 0
        self.input_char_list_end = len(self.input_s.char_list)
        self.update_index_and_show_s()

        kl = KeyListener()

        kl.bind_key('any', self.key_event, decorator=False)

        kl.listen()
        self.move_cursor_to_btm()

        if self.ctl.auto_re_draw:
            self.ctl.init_refresh_thread()
            self.ctl.refresh_thread.start()

        return str(self.input_s)

    def move_cursor_to_view(self):
        s = ''
        if self.layout_height - self.x > 0:
            s += Cursor.UP(self.layout_height - self.x)
        if self.y + self.cursor_index > 0:
            s += Cursor.FORWARD(self.y + self.cursor_index)
        if s:
            sys.stdout.write(s)
            sys.stdout.flush()

    def char_list_iter(self, i, reverse):
        for i in range(i - 1, -1, -1) if reverse else range(i, len(self.input_s.char_list), 1):
            yield i, self.input_s.char_list[i]

    def update_index_and_show_s(self, right=True):
        """
        right: 光标从左向右移动
        """

        if len(self.input_s) >= self.max_width:
            left_width = self.max_width
            if right:
                list_iter = self.char_list_iter(self.input_char_list_end, True)
            else:
                list_iter = self.char_list_iter(self.input_char_list_index, False)

            new_i = 0
            for i, c in list_iter:
                logger.info(f'list_iter | i={i}, c={c}, len(c)={len(c)}, left_width={left_width} ')

                if left_width - len(c) < 0:
                    break
                left_width -= len(c)
                new_i = i

            if right:
                self.input_char_list_start = new_i
                # self.input_char_list_end = new_i + self.max_width
            else:
                self.input_char_list_end = new_i + 1
                # self.input_char_list_start = new_i + 1 - self.max_width
        logger.info(
            f'input_char_list_start={self.input_char_list_start}, input_char_list_end={self.input_char_list_end} ')

        self.cursor_index = 0
        show_s = ''
        for i in range(self.input_char_list_start, self.input_char_list_end):
            show_s += str(self.input_s.char_list[i])
            if i < self.input_char_list_index:
                self.cursor_index += len(self.input_s.char_list[i])

        logger.info(
            f'input_char_list_index={self.input_char_list_index}, cursor_index={self.cursor_index}, show_s={show_s}')

        self.move_cursor_to_btm()
        self.view.set_text(show_s)
        self.ctl.re_draw()
        self.move_cursor_to_view()

    def move_cursor_to_btm(self):
        s = ''
        if self.layout_height - self.x > 0:
            s += Cursor.DOWN(self.layout_height - self.x)
        if self.y + self.cursor_index > 0:
            s += Cursor.BACK(self.y + self.cursor_index + 2)
        if s:
            sys.stdout.write(s)
            sys.stdout.flush()

    def update_text(self):

        self.view.set_text(str(self.input_s))
        self.ctl.update_width()

    def key_event(self, kl, event):
        c = event.key.code
        right = True

        if len(repr(c)) > 1 and (repr(c).startswith("'\\") or repr(c).startswith("u'\\")):
            if event.key == Key.LEFT and self.input_char_list_index > 0:

                self.input_char_list_index -= 1
                if self.input_char_list_index < self.input_char_list_start:
                    self.input_char_list_start = self.input_char_list_index
                    right = False

            elif event.key == Key.RIGHT and self.input_char_list_index < len(self.input_s.char_list):

                self.input_char_list_index += 1
                if self.input_char_list_index > self.input_char_list_end - 1:
                    self.input_char_list_end = min(self.input_char_list_index + 1, len(self.input_s.char_list))

            elif event.key == Key.BACKSPACE and self.input_char_list_index > 0:

                self.input_char_list_index -= 1
                self.input_s.pop(self.input_char_list_index)
                self.input_char_list_end -= 1

            elif event.key == Key.ENTER:
                kl.stop()
                return
        else:

            c_str = String(c)

            self.input_s.insert_into_char_list(self.input_char_list_index, c_str)
            self.input_char_list_index += len(c_str.char_list)
            self.input_char_list_end += len(c_str.char_list)
            logger.info(f'insert {c_str}, {self.input_char_list_index}, {self.input_char_list_end}')

        self.update_index_and_show_s(right=right)

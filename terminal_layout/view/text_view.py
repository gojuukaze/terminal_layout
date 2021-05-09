# -*- coding: utf-8 -*-
import sys
import threading

from terminal_layout.ansi import *
from terminal_layout.types import String
from terminal_layout.view.base import View
from terminal_layout.view.params import Visibility, Width, Gravity, Overflow


class TextView(View):
    __slots__ = ('back', 'style', 'fore', 'text', 'text_string', 'weight', 'overflow')

    def __init__(self, id, text, fore=None, back=None, style=None, width=Width.wrap,
                 height=1, weight=None, visibility=Visibility.visible, gravity=Gravity.left,
                 overflow=Overflow.hidden_right):
        """

        :param id:
        :param width:
        :param height: no used

        :type id:str
        :type width: Union[int, str]
        :type height:int
        :type visibility:str
        :type gravity:str
        :type overflow:str

        """

        super(TextView, self).__init__(id, width, height, visibility, gravity)
        self.text_string = None  # type:String

        self.text = text
        self.fore = fore or ''
        self.back = back or ''
        self.style = style or ''
        self.weight = weight
        self.overflow = overflow

        self.real_height = 1

    def update_width(self, parent_width):
        if parent_width <= 0:
            self.real_width = 0
            return self.real_width
        if self.weight:
            return None
        if isinstance(self.width, int) and self.width >= 0:
            self.real_width = int(self.width)
            temp = parent_width - self.real_width
            if temp <= 0:
                self.real_width = parent_width

        elif self.width == Width.wrap:
            self.real_width = len(self.text_string)
            temp = parent_width - self.real_width
            if temp <= 0:
                self.real_width = parent_width

        elif self.width == Width.fill:
            self.real_width = parent_width

        return self.real_width

    def draw(self):
        sys.stdout.write(self.get_final_text())

    def clear(self):
        sys.stdout.write(Cursor.UP(self.real_height) + clear_line())

    def get_final_text(self):

        if self.visibility == Visibility.visible:
            self.real_height = 1
            show_text = self.text_string[:self.real_width] if self.overflow == Overflow.hidden_right \
                else self.text_string[-self.real_width:]
        elif self.visibility == Visibility.invisible:
            self.real_height = 1
            return ' ' * self.real_width
        elif self.visibility == Visibility.gone:
            return ''

        # show_text是str 要转为String
        show_string = String(show_text)
        if self.real_width > len(show_string):
            if self.gravity == Gravity.left:
                show_text = show_text + ' ' * (self.real_width - len(show_string))
            elif self.gravity == Gravity.right:
                show_text = ' ' * (self.real_width - len(show_string)) + show_text
            elif self.gravity == Gravity.center:
                p = (self.real_width - len(show_string)) / 2.0
                show_text = ' ' * int(p) + show_text + ' ' * (int(p) if int(p) == p else int(p) + 1)

        return str(self.fore) + str(self.back) + str(self.style) + show_text + str(Style.reset_all)

    def __str__(self):
        return str(self.fore) + str(self.back) + str(self.style) + self.text + str(Style.reset_all)

    def __setattr__(self, key, value):
        super(TextView, self).__setattr__(key, value)
        if key == 'text':
            self.text_string = String(value)


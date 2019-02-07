# -*- coding: utf-8 -*-
import sys

from terminal_layout.ansi import *
from terminal_layout.types import String
from terminal_layout.view.base import View
from terminal_layout.view.params import Visibility, Width, Gravity


class TextView(View):
    string_text = None  # type:String

    def __init__(self, id, text, fore=None, back=None, style=None, width=Width.wrap,
                 height=1, weight=None, visibility=Visibility.visible, gravity=Gravity.left):
        """

        :param id:
        :param width:
        :param height: no used

        :type id:str
        :type width:
        :type height:int
        :type visibility:str
        :type gravity:str
        """

        super(TextView, self).__init__(id, width, height, visibility, gravity)

        self.text = text
        self.fore = fore or ''
        self.back = back or ''
        self.style = style or ''
        self.weight = weight

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
            self.real_width = len(self.string_text)
            temp = parent_width - self.real_width
            if temp <= 0:
                self.real_width = parent_width

        elif self.width == Width.fill:
            self.real_width = parent_width

        return self.real_width

    def draw(self):
        sys.stdout.write(self.get_final_text())

    def re_draw(self):
        self.draw()

    def get_final_text(self):

        if self.visibility == Visibility.visible:
            show_text = self.string_text[:self.real_width]
        elif self.visibility == Visibility.invisible:
            show_text = ' ' * self.real_width
        elif self.visibility == Visibility.gone:
            return ''

        text = String(show_text)
        if self.real_width > len(text):
            if self.gravity == Gravity.left:
                show_text = show_text + ' ' * (self.real_width - len(text))
            elif self.gravity == Gravity.right:
                show_text = ' ' * (self.real_width - len(text)) + show_text
            elif self.gravity == Gravity.center:
                p = (self.real_width - len(text)) / 2.0
                show_text = ' ' * int(p) + show_text + ' ' * (int(p) if int(p) == p else int(p) + 1)

        return str(self.fore) + str(self.back) + str(self.style) + show_text + str(Style.reset_all)

    def __str__(self):
        return str(self.fore) + str(self.back) + str(self.style) + self.text + str(Style.reset_all)

    def __setattr__(self, key, value):
        super(TextView, self).__setattr__(key, value)
        if key == 'text':
            self.string_text = String(value)

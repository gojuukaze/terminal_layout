# -*- coding: utf-8 -*-
import os
from terminal_layout.ansi import term_init
from terminal_layout.view import *
from terminal_layout.view.base import View


class LayoutCtl(object):
    debug = False

    def __init__(self, layout):
        self.layout = layout  # type:View

    @classmethod
    def quick(cls, layout_class, data):
        """

        :param layout_class:
        :param data:
        :return:
        :rtype :LayoutCtl
        """
        if layout_class is not TableLayout:
            raise TypeError("only support TableLayout")

        table_layout = TableLayout('', Width.fill)
        for row_data in data:
            table_row = TableRow('', Width.fill)
            table_row.add_view_list(row_data)
            table_layout.add_view(table_row)
        return cls(table_layout)

    def get_layout(self):
        """

        :return:
        :rtype:View
        """
        return self.layout

    def get_terminal_size(self):
        if self.debug:
            self.height = 10
            self.width = 50
            return
        try:
            size = os.get_terminal_size()
            self.height = size.lines
            self.width = size.columns
        except:
            # py2
            from terminal_layout.helper import get_terminal_size
            self.height, self.width = get_terminal_size()

    def update_width(self):
        self.get_terminal_size()
        self.layout.update_width(self.width)

    def draw(self):
        term_init()
        self.update_width()
        self.layout.draw()

    def re_draw(self):
        self.update_width()
        self.layout.re_draw()

    def find_view_by_id(self, id):
        return self.layout.find_view_by_id(id)

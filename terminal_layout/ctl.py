# -*- coding: utf-8 -*-
import os
import sys
import platform
from terminal_layout.ansi import term_init
from terminal_layout.view import *
from terminal_layout.view.base import View


class LayoutCtl(object):
    debug = False

    def __init__(self, layout=None):
        self.layout = layout  # type:View

    @classmethod
    def quick(cls, layout_class, data):
        """

        :param layout_class:
        :param data:
        :return:
        :rtype :LayoutCtl
        """
        if layout_class is TableLayout:

            table_layout = TableLayout('', Width.fill)
            for row_data in data:
                table_row = TableRow.quick_init('', row_data, width=Width.fill)
                table_layout.add_view(table_row)
            return cls(table_layout)
        elif layout_class is TableRow:
            row = TableRow.quick_init('', data, width=Width.fill)
            return cls(row)
        else:
            raise TypeError("quick not support %s" % (str(layout_class, )))

    def set_layout(self, layout):
        """

        :return:
        """

        self.layout = layout

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
            from backports.shutil_get_terminal_size import get_terminal_size
            size = os.get_terminal_size()
            self.height = size.lines
            self.width = size.columns

        if platform.system() == 'Windows':
            self.width -= 1

    def update_width(self):
        self.get_terminal_size()
        self.layout.update_width(self.width)

    def draw(self):
        term_init()
        self.update_width()
        self.layout.draw()

        sys.stdout.write('\n')
        sys.stdout.flush()

    def clear(self):
        self.layout.clear()

    def re_draw(self):
        self.clear()

        self.update_width()
        self.layout.draw()

        sys.stdout.write('\n')
        sys.stdout.flush()

    def find_view_by_id(self, id):
        return self.layout.find_view_by_id(id)

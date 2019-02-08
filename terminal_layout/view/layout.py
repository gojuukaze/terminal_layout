# -*- coding: utf-8 -*-

import subprocess
import os
import sys

from terminal_layout.ansi import Cursor, clear_line, Style
from terminal_layout.view.base import View
from terminal_layout.view.params import Visibility, Gravity, Orientation, Width
from terminal_layout.view.text_view import TextView


class TableRow(View):
    data = None  # type:list[TextView]

    def __init__(self, id, width=Width.fill, height=1, back=None, visibility=Visibility.visible, gravity=Gravity.left):
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

        super(TableRow, self).__init__(id, width, height, visibility, gravity)
        self.back = back or ''

    @classmethod
    def quick_init(cls, id, data, width=Width.fill, height=1, back=None, visibility=Visibility.visible,
                   gravity=Gravity.left):
        """

        :param id:
        :param data:
        :param width:
        :param height:
        :param back:
        :param visibility:
        :param gravity:
        :return:

        :rtype:TableRow
        """

        row = cls(id, width, height, back, visibility, gravity)
        row.data = data
        return row

    def add_view(self, v):
        if not isinstance(v, TextView):
            raise TypeError('must be TextView')
        self.data.append(v)

    def add_view_list(self, views):
        self.data += views

    def draw(self):
        if self.visibility == Visibility.visible:
            left = ''
            right = ''
            if self.real_width > self.child_width:
                if self.gravity == Gravity.left:
                    right = ' ' * (self.real_width - self.child_width)
                elif self.gravity == Gravity.right:
                    left = ' ' * (self.real_width - self.child_width)
                elif self.gravity == Gravity.center:
                    p = (self.real_width - self.child_width) / 2.0
                    left = ' ' * int(p)
                    right = ' ' * (int(p) if int(p) == p else int(p) + 1)
            sys.stdout.write(str(self.back) + left + str(Style.reset_all))
            for v in self.data:
                v.draw()
            sys.stdout.write(str(self.back) + right + str(Style.reset_all))
        elif self.visibility == Visibility.invisible:
            sys.stdout.write(' ' * self.real_width)

    def re_draw(self):
        self.draw()

    def update_width(self, parent_width):
        """

        :param parent_width:
        :return:
        :rtype:int
        """

        if self.width == Width.fill:
            self.real_width = parent_width
        elif self.width == Width.wrap:
            pass
        else:
            self.real_width = self.width

        weight_view = []
        all_weight = 0

        if self.width == Width.wrap:
            _width = parent_width
        else:
            _width = self.real_width

        for v in self.data:
            if v.weight:
                weight_view.append(v)
                all_weight += v.weight
                continue
            child_width = v.update_width(_width)
            _width -= child_width
            _width = max(0, _width)

        if weight_view:
            per_weight = _width / float(all_weight)
            for v in weight_view:
                v.real_width = int(v.weight * per_weight)

        self.child_width = sum([v.real_width for v in self.data])

        if self.width == Width.wrap:
            self.real_width = self.child_width

        return self.real_width


class TableLayout(View):
    data = None  # type: list[TableRow]

    def __init__(self, id, width=Width.fill, height=1, visibility=Visibility.visible):
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

        super(TableLayout, self).__init__(id, width, height, visibility, Gravity.left)

    @classmethod
    def quick_init(cls, id, data, width=Width.fill, height=1, visibility=Visibility.visible):
        """

        :param id:
        :param data:
        :param width:
        :param height:
        :param visibility:
        :return:

        :rtype:TableLayout
        """

        table = cls(id, width, height, visibility)
        table.data = data
        return table

    def add_view(self, v):
        if not isinstance(v, TableRow):
            raise TypeError('must be TableRow')
        self.data.append(v)

    def add_view_list(self, views):
        self.data += views

    def update_width(self, parent_width):
        """

        :param parent_width:
        :return:
        :rtype: int
        """

        if self.width == Width.fill:
            self.real_width = parent_width
        elif self.width == Width.wrap:
            self.real_width = 0
        else:
            self.real_width = self.width

        for row in self.data:
            if self.width == Width.wrap:
                child_width = row.update_width(parent_width)
                self.real_width = max(self.real_width, child_width)
            else:
                row.update_width(self.real_width)

        return self.real_width

    def draw(self):
        self.draw_height = 0
        for r in self.data:
            if r.visibility != Visibility.gone:
                r.draw()
                sys.stdout.write('\n')
                self.draw_height += 1
        sys.stdout.flush()

    def re_draw(self):

        sys.stdout.write(Cursor.UP(self.draw_height) + clear_line())
        self.draw()


class LinearLayout(View):

    def __init__(self, id, width, height=1, visibility=Visibility.visible, gravity=Gravity.left,
                 orientation=Orientation.vertical):
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

        super(LinearLayout, self).__init__(id, width, height, visibility, gravity)
        if orientation == Orientation.vertical:
            self.end_code = '\n'
        elif orientation == Orientation.horizon:
            self.end_code = ''

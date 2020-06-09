# -*- coding: utf-8 -*-

import sys

from terminal_layout.ansi import Cursor, clear_line, Style
from terminal_layout.view.base import View
from terminal_layout.view.params import Visibility, Gravity, Orientation, Width
from terminal_layout.view.text_view import TextView


class TableRow(View):
    __slots__ = ('back', 'child_width')

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
        self.data = []  # type:list[TextView]

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
            raise TypeError('only support add TextView')
        self.data.append(v)

    def add_views(self, *views):
        self.data += views

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
            self.real_height = 1
        elif self.visibility == Visibility.invisible:
            sys.stdout.write(' ' * self.real_width)
            self.real_height = 1

    def clear(self):
        sys.stdout.write(Cursor.UP(self.real_height) + clear_line())

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
            per_width = _width / float(all_weight)
            for v in weight_view:
                v.real_width = int(v.weight * per_width)

        self.child_width = sum([v.real_width for v in self.data])

        if self.width == Width.wrap:
            self.real_width = self.child_width

        return self.real_width


class TableLayout(View):

    def __init__(self, id, width=Width.fill, height=1, visibility=Visibility.visible):
        """

        :param id:
        :param width:
        :param height: no used

        :type id:str
        :type width:
        :type height:int
        :type visibility:str
        """

        super(TableLayout, self).__init__(id, width, height, visibility, Gravity.left)
        self.data = []  # type: list[TableRow]

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

        self.data.append(v)

    def add_views(self, *views):

        self.data += views

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
        self.real_height = 0
        is_first = True
        for r in self.data:
            if r.visibility != Visibility.gone:
                if not is_first:
                    sys.stdout.write('\n')
                else:
                    is_first = False
                r.draw()
                self.real_height += 1

    def clear(self):
        while self.real_height:
            sys.stdout.write(Cursor.UP(1) + clear_line())
            self.real_height -= 1


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

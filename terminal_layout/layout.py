# -*- coding: utf-8 -*-

import subprocess
import os


class Layout(object):

    def __init__(self, layout: list):
        if not isinstance(layout, list):
            raise TypeError('views must be list')
        for l in layout:
            if isinstance(l, list):
                raise TypeError('item in views must be list')

        self.layout = layout

    def show(self):
        size = os.get_terminal_size()
        height = size.lines
        width = size.columns

        for line_layout in self.layout:
            for v in line_layout:
                v.
                print(v, end='')

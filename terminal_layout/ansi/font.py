# -*- coding: utf-8 -*-
from colorama.ansi import code_to_chars
from colored import fg, bg, attr


class Font(object):
    ex_function = {
        'fore': fg,
        'back': bg,
        'style': attr
    }

    def __init__(self, name, type, code=None):
        """

        :param name: color name or style name
        :param type: fore ,back , style
        :param code: colorama color,style num
        """
        self.name = name
        self.type = type
        self.code = code

    def __str__(self):
        if not self.name:
            return ''
        if self.name.startswith('ex_'):
            func = self.ex_function[self.type]
            return func(self.name[3:])
        else:
            return code_to_chars(self.code)

    def __add__(self, other):
        print('add')
        return str(self) + str(other)

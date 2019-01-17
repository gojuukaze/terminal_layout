# -*- coding: utf-8 -*-
from terminal_layout.helper import is_ascii


class ViewChar(str):
    length = None

    char_to_length = {
        '\t': 4,
        '\n': 1,
    }

    char_to_str = {
        '\t': ' ' * 4,
        '\n': ' ',
    }

    def __init__(self, c):
        super().__init__()
        if len(c) != 1:
            raise TypeError('expected a character, but string of length %d found' % len(c))
        self.c = c

    def __len__(self):
        if self.length is not None:
            return self.length

        if is_ascii(self.c):
            self.length = 1
        else:
            self.length = 2
        return self.length

    def __str__(self):
        return self.char_to_str.get(self.c, self.c)


class ViewString(str):
    length = None
    text_list = []

    def __init__(self, text: str):
        super().__init__()
        for c in text:
            self.text_list.append(ViewChar(c))

    def __len__(self):
        if self.length is not None:
            return self.length

        t = 0
        for c in self.text_list:
            t += len(c)
        self.length = t

        return self.length

    def __str__(self):
        return ''.join(self.text_list)


class l(list):

    def __
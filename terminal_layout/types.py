# -*- coding: utf-8 -*-
from terminal_layout.helper import is_ascii


class Char(object):
    length = None

    char_to_length = {
        '\t': 4,
    }

    char_to_str = {
        '\t': ' ' * 4,
        '\n': ' ',
    }

    def __init__(self, c):
        if len(c) != 1:
            raise TypeError('expected a character, but string of length %d found' % len(c))
        self.c = c

    def __len__(self):
        if self.length is not None:
            return self.length

        temp = self.char_to_length.get(self.c, None)
        if temp:
            self.length = temp
            return self.length

        if is_ascii(self.c):
            self.length = 1
        else:
            self.length = 2
        return self.length

    def __str__(self):
        return self.char_to_str.get(self.c, self.c)


class String(object):
    """

    ex:

    >>> s=String('a啊啊')
    >>> len(s)
    5
    >>> s[:2]
    'a'
    >>> s[:3]
    'a啊'

    """
    length = None
    char_list = None

    def __init__(self, text):
        """

        :param text:
        :type text:str
        """
        self.char_list = []  # type: list[Char]
        self.origin_text = text
        for c in text:
            self.char_list.append(Char(c))

    def __len__(self):
        if self.length is not None:
            return self.length

        t = 0
        for c in self.char_list:
            t += len(c)
        self.length = t

        return self.length

    def __str__(self):
        return ''.join(str(c) for c in self.char_list)

    def __getitem__(self, item):
        start = item.start or 0
        if start != 0:
            raise TypeError('slice start must be 0 or None')
        stop = item.stop
        if stop is None or stop < 0:
            raise TypeError('slice stop must be positive integer')

        s = ''
        for c in self.char_list:
            length = len(c)
            if stop >= length:
                s += str(c)
            else:
                break
            stop -= length

        return s

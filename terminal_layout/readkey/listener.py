import re
import sys
from datetime import datetime

from terminal_layout.readkey.key import Key, KeyInfo
from terminal_layout.readkey.event import KeyPressEvent

if sys.platform in ('win32', 'cygwin'):
    from terminal_layout.readkey.windows import readkey as _readkey
else:
    from terminal_layout.readkey.linux import readkey as _readkey


def get_code_to_name():
    """
    :return:
    :rtype: dict
    """
    d = {}
    for k, info in Key.__dict__.items():
        if not k.startswith("_"):
            d[info.code] = info.name
    return d


code_to_name = get_code_to_name()


def readkey():
    c = _readkey()
    n = datetime.now()
    name = code_to_name.get(c, None)
    if name:
        return KeyPressEvent(KeyInfo(name, c), n)
    if repr(c).startswith("'\\x") or repr(c).startswith("u'\\x"):
        return KeyPressEvent(KeyInfo('unknown', c), n)
    else:
        return KeyPressEvent(KeyInfo(c, c), n)


class KeyListener(object):

    def __init__(self):
        self.key_func = {}
        self.re_func = {}
        self.stop_flag = False

    def bind_key(self, *args, **kwargs):
        """
        args: key or regular expression;
        :param args:
        :param kwargs:
        """
        decorator = kwargs.get('decorator', True)
        if decorator:
            keys = args
        else:
            keys = args[:-1]

        def inner(func):
            for k in keys:
                if isinstance(k, KeyInfo):
                    self.key_func[k.code] = func
                elif isinstance(k, str):
                    self.re_func[k] = func
                else:
                    raise TypeError('item in *args must be a KeyInfo or a regular expression string')
            return func

        if decorator:
            return inner
        else:
            inner(args[-1])

    def stop(self):
        self.stop_flag = True

    def listen(self, stop_key=None):
        """

        :param stop_key: key or regular expression; default [Key.ESC]
        :type stop_key: list
        :return: 
        :rtype: 
        """
        if stop_key is None:
            stop_key = [Key.ESC]

        while True:
            if self.stop_flag:
                break
            c = readkey()
            code = c.key.code
            for s in stop_key:
                if isinstance(s, KeyInfo):
                    if s.code == code:
                        return
                else:
                    if re.match(s, code):
                        return

            func = self.key_func.get(c.key.code, None)
            if func:
                func(self, c)

            for s, func in self.re_func.items():
                if s == 'any':
                    func(self, c)
                    continue
                if re.match(s, code):
                    func(self, c)
                    continue

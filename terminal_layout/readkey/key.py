class KeyInfo:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __eq__(self, other):
        if isinstance(other, KeyInfo):
            return self.code == other.code
        return self.code == other

    def __str__(self):
        return '<%s>' % self.name
    def __repr__(self):
        return self.__str__()

class Key:
    ENTER = KeyInfo('enter', '\r')
    TAB = KeyInfo('tab', '\x09')
    BACKSPACE = KeyInfo('backspace', '\x7f')
    ESC = KeyInfo('esc', '\x1b')

    UP = KeyInfo('up', '\x1b[A')
    DOWN = KeyInfo('down', '\x1b[B')
    LEFT = KeyInfo('left', '\x1b[D')
    RIGHT = KeyInfo('right', '\x1b[C')

    CTRL_A = KeyInfo('ctrl_a', '\x01')
    CTRL_B = KeyInfo('ctrl_b', '\x02')
    CTRL_C = KeyInfo('ctrl_c', '\x03')
    CTRL_D = KeyInfo('ctrl_d', '\x04')
    CTRL_E = KeyInfo('ctrl_e', '\x05')
    CTRL_F = KeyInfo('ctrl_f', '\x06')
    CTRL_X = KeyInfo('ctrl_x', '\x18')
    CTRL_Z = KeyInfo('ctrl_z', '\x1a')

    F1 = KeyInfo('f1', '\x1bOP')
    F2 = KeyInfo('f2', '\x1bOQ')
    F3 = KeyInfo('f3', '\x1bOR')
    F4 = KeyInfo('f4', '\x1bOS')
    F5 = KeyInfo('f5', '\x1b[15')
    F6 = KeyInfo('f6', '\x1b[17')
    F7 = KeyInfo('f7', '\x1b[18')
    F8 = KeyInfo('f8', '\x1b[19')

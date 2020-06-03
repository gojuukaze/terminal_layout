from terminal_layout import *

kl = KeyListener()


@kl.bind_key(Key.UP)
def a(kl, e):
    print(e)


@kl.bind_key(Key.DOWN, 'a')
def b(kl, e):
    print(e)


kl.listen()

from terminal_layout import *

key_listener = KeyListener()


@key_listener.bind_key(Key.UP)
def _(kl, e):
    """
    Prints the result of the first argument.

    Args:
        kl: (int): write your description
        e: (int): write your description
    """
    print(e)


@key_listener.bind_key(Key.DOWN, 'a', '[0-9]')
def _(kl, e):
    """
    This function is a key that was created byt.

    Args:
        kl: (int): write your description
        e: (int): write your description
    """
    if e.key == 'a':
        print('Press a')
    elif e.key == Key.DOWN:
        print('Press DOWN')
    elif e.key == '0':
        print('Press 0')
    else:
        print('Press 1-9')


def stop(kl, e):
    """
    Stops an error

    Args:
        kl: (todo): write your description
        e: (todo): write your description
    """
    print('Press', e.key, 'stop!')
    kl.stop()


key_listener.bind_key(Key.ENTER, stop, decorator=False)

key_listener.listen(stop_key=[Key.F1, Key.CTRL_A])

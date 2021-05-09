from terminal_layout import *
from terminal_layout.extensions.input import *

ctl = LayoutCtl.quick(TableRow,
                      [TextView('', 'Input Something: ', fore=Fore.magenta),
                       TextView('input', '', width=11, fore=Fore.blue)])
ctl.draw()
ok, s = InputEx(ctl).get_input('input')
if ok:
    print('-------')
    print('Your input:', Fore.blue, s, Fore.reset)
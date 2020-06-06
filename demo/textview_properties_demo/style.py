# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from terminal_layout import *

print('\nstyle support window, linux, osx\n')

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'style = bright', style=Style.bright)],
                          [TextView('', 'style = dim', style=Style.dim)],
                          [TextView('', 'style = normal', style=Style.normal)]
                      ])

ctl.draw(auto_re_draw=False)


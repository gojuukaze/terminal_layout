# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from terminal_layout import *

print('\n[ex]style support linux, osx\n')

ctl = LayoutCtl.quick(TableLayout,
                      [[TextView('', 'style = ex_bold', style=Style.ex_bold)],
                       [TextView('', 'style = ex_dim', style=Style.ex_dim)],
                       [TextView('', 'style = ex_underlined', style=Style.ex_underlined)],
                       [TextView('', 'style = ex_blink', style=Style.ex_blink)],
                       [TextView('', 'style = ex_reverse', style=Style.ex_reverse)],
                       ])

ctl.draw(auto_re_draw=False)

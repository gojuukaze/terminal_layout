# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'weight = 1 ', weight=1, back=Back.cyan),
                           TextView('', 'weight = 1 ', weight=1, back=Back.green)],
                          [TextView('', 'weight = 3 ', weight=3, back=Back.cyan),
                           TextView('', 'weight = 1 ', weight=1, back=Back.green)],
                          [TextView('', 'weight = 1 ', weight=1, back=Back.cyan),
                           TextView('', 'width = 15 ', width=15, back=Back.green)],
                          [TextView('', 'weight = 2 ', weight=1, back=Back.cyan),
                           TextView('', 'width = 15 ', width=15, back=Back.green)],
                          [TextView('', 'weight = 1 ', weight=1, back=Back.cyan),
                           TextView('', 'width = wrap ', width=Width.wrap, back=Back.green)],

                      ])

t = ctl.get_layout()
t.set_width(40)

ctl.draw(auto_re_draw=False)

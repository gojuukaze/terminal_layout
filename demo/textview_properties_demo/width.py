# -*- coding: utf-8 -*-
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'width = 12', width=12, back=Back.green)],
                          [TextView('', 'width = warp', width=Width.wrap, back=Back.green)],
                          [TextView('', 'width = fill', width=Width.fill, back=Back.green)],
                      ])

ctl.get_layout().set_width(50)

ctl.draw(auto_re_draw=False)

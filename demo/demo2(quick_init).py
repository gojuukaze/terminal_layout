# -*- coding: utf-8 -*-

from terminal_layout import *

title_view = TextView('title', 'Title', width=Width.wrap)

row1 = TableRow.quick_init('row1', [title_view], width=Width.fill, gravity=Gravity.center)

data1_view = TextView('data1', '1.', width=3)
data2_view = TextView('data2', 'abcdefghijk', width=5)

row2 = TableRow.quick_init('row2', [data1_view, data2_view])

table_layout = TableLayout.quick_init('', [row1, row2], width=10)

ctl = LayoutCtl(table_layout)

ctl.draw()

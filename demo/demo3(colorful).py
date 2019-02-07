# -*- coding: utf-8 -*-

from terminal_layout import *

title_view = TextView('title', 'Title', width=Width.wrap, fore=Fore.red, back=Back.yellow)

row1 = TableRow.quick_init('row1', [title_view], width=Width.fill, gravity=Gravity.center, back=Back.cyan)

data1_view = TextView('data1', 'A.', width=3, back=Back.green, style=Style.bright)
data2_view = TextView('data2', 'abcdefghijk', width=5, back=Back.red)

row2 = TableRow.quick_init('row2', [data1_view, data2_view])

row3 = TableRow.quick_init('row2', [TextView('', 'A.', width=3, back=Back.green, style=Style.dim), data2_view])

row4 = TableRow.quick_init('row2', [TextView('', 'A.', width=3, back=Back.green, style=Style.normal), data2_view])

table_layout = TableLayout.quick_init('', [row1, row2, row3, row4], width=10)

ctl = LayoutCtl(table_layout)

ctl.draw()

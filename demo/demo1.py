# -*- coding: utf-8 -*-
from terminal_layout import *

# new table layout
table_layout = TableLayout('table_layout', width=10)

# new table row
row1 = TableRow('row1', width=Width.fill, gravity=Gravity.center)

# new text view
title_view = TextView('title', 'Title', width=Width.wrap)

# add text view
row1.add_view(title_view)

#
row2 = TableRow('row2', width=Width.fill)

data1_view = TextView('data1', '1.', width=3)
data2_view = TextView('data2', 'abcdefghijk', width=5)

row2.add_view_list([data1_view, data2_view])

# add row
table_layout.add_view(row1)
table_layout.add_view(row2)

# new layout ctl
ctl = LayoutCtl(table_layout)

# draw
ctl.draw()

# -*- coding: utf-8 -*-
from terminal_layout import *
import time

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('title', 'Student', fore=Fore.black, back=Back.yellow, width=17,
                                    gravity=Gravity.center)],

                          [TextView('', 'No.', width=5, back=Back.yellow),
                           TextView('', 'Name', width=12, back=Back.yellow)],

                          [TextView('st1_no', '1', width=5, back=Back.yellow),
                           TextView('st1_name', 'Bob', width=12, back=Back.yellow)],

                          [TextView('st2_no', '2', width=5, back=Back.yellow),
                           TextView('st2_name', 'Tom', width=12, back=Back.yellow)],

                          [TextView('tip', 'modify name of no.2 after 2s', width=Width.wrap)]
                      ]

                      )

ctl.draw()

tip = ctl.find_view_by_id('tip')
time.sleep(1)
tip.text='modify name of no.2 after 1s'
ctl.re_draw()
time.sleep(1)

# modify name

st2_name = ctl.find_view_by_id('st2_name')

st2_name.text = 'New Tom'
tip.text = 'add a new row after 2s'
ctl.re_draw()

time.sleep(1)
tip.text = 'add a new row after 1s'
ctl.re_draw()
time.sleep(1)



# add row

row = TableRow.quick_init('',
                          [TextView('st3_no', '3', width=5, back=Back.yellow),
                           TextView('st3_name', '李', width=12, back=Back.yellow)])

table = ctl.get_layout()

table.insert(4, row)

tip.text = 'set row2 invisible after 2s'

ctl.re_draw()

time.sleep(1)
tip.text = 'set row2 invisible after 1s'
ctl.re_draw()
time.sleep(1)


# invisible

table[3].visibility = Visibility.invisible

tip.text = 'set row2 gone after 2s'
ctl.re_draw()

time.sleep(1)
tip.text = 'set row2 gone after 1s'
ctl.re_draw()
time.sleep(1)

# gone

table[3].visibility = Visibility.gone

ctl.re_draw()

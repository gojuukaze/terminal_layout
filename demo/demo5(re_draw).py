# -*- coding: utf-8 -*-
from terminal_layout import *
import time

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('title', 'Student', fore=Fore.black, back=Back.blue, width=17,
                                    gravity=Gravity.center)],

                          [TextView('', 'No.', width=5, back=Back.blue),
                           TextView('', 'Name', width=12, back=Back.blue)],

                          [TextView('st1_no', '1', width=5, back=Back.blue),
                           TextView('st1_name', 'Bob', width=12, back=Back.blue)],

                          [TextView('st2_no', '2', width=5, back=Back.blue),
                           TextView('st2_name', 'Tom', width=12, back=Back.blue)],

                          [TextView('tip', 'modify name of no.2 after 2s', width=Width.wrap)]
                      ]

                      )

ctl.draw()

tip = ctl.find_view_by_id('tip')
time.sleep(1)
tip.set_text('modify name of no.2 after 1s')
ctl.re_draw()
time.sleep(1)

# modify name

st2_name = ctl.find_view_by_id('st2_name')

st2_name.set_text('New Tom')
tip.set_text('add a new row after 2s')
ctl.re_draw()

time.sleep(1)
tip.set_text('add a new row after 1s')
ctl.re_draw()
time.sleep(1)



# add row

row = TableRow.quick_init('',
                          [TextView('st3_no', '3', width=5, back=Back.blue),
                           TextView('st3_name', '李', width=12, back=Back.blue)])

table = ctl.get_layout()

table.insert_view(4, row)

tip.set_text('set row2 invisible after 2s')

ctl.re_draw()

time.sleep(1)
tip.set_text('set row2 invisible after 1s')
ctl.re_draw()
time.sleep(1)


# invisible

ctl.find_view_by_id('root_row_3').set_visibility(Visibility.invisible)

tip.set_text('set row2 gone after 2s')
ctl.re_draw()

time.sleep(1)
tip.set_text( 'set row2 gone after 1s')
ctl.re_draw()
time.sleep(1)

# gone

ctl.find_view_by_id('root_row_3').set_visibility( Visibility.gone)

ctl.re_draw()

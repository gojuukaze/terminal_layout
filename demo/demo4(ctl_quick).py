# -*- coding: utf-8 -*-
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('title', 'Student', fore=Fore.black, back=Back.yellow, width=17,
                                    gravity=Gravity.center)],

                          [TextView('', 'No.', width=5, back=Back.yellow),
                           TextView('', 'Name', width=12, back=Back.yellow)],

                          [TextView('st1_no', '1', width=5, back=Back.yellow),
                           TextView('st1_name', 'Bob', width=12, back=Back.yellow)],

                          [TextView('stw_no', '2', width=5, back=Back.yellow),
                           TextView('st1_name', 'Tom', width=12, back=Back.yellow)]
                      ]

                      )

ctl.draw()

print('\n')

ctl = LayoutCtl.quick(TableRow,

                      [TextView('', 'row1', width=5, back=Back.yellow),
                       TextView('', 'data', width=12, back=Back.yellow)]

                      )

ctl.draw()

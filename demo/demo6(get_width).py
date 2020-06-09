# -*- coding: utf-8 -*-
from terminal_layout import *
import time


def show_width(w1, w2, w3):
    for w in [w1, w2, w3]:
        print('%s: width=%s ,real_width=%s' % (w.get_id(), str(w.get_width()), str(w.get_real_width())))


ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('w1', 'w1: width=15', back=Back.cyan, width=20)],
                          [TextView('w2', 'w2: width=fill', back=Back.cyan, width=Width.fill)],
                          [TextView('w3', 'w3: width=warp', back=Back.cyan, width=Width.wrap)],
                      ]

                      )

w1 = ctl.find_view_by_id('w1')
w2 = ctl.find_view_by_id('w2')
w3 = ctl.find_view_by_id('w3')

print(str(Fore.green) + "get width before draw()" + str(Style.reset_all))
show_width(w1, w2, w3)

print('==================')
print(str(Fore.green) + "get width after draw()" + str(Style.reset_all))

ctl.draw(auto_re_draw=False)

show_width(w1, w2, w3)
print('==================')

#
ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('w1', 'w1: width=15', back=Back.cyan, width=20)],
                          [TextView('w2', 'w2: width=fill', back=Back.cyan, width=Width.fill)],
                          [TextView('w3', 'w3: width=warp', back=Back.cyan, width=Width.wrap)],
                      ]

                      )
print(str(Fore.green) + "get width after update_width()" + str(Style.reset_all))

ctl.update_width()

show_width(w1, w2, w3)

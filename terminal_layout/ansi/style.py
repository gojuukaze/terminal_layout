# -*- coding: utf-8 -*-
from terminal_layout.ansi.font import Font


class Style(object):

    bright = Font('bright', 'style', 1)
    dim = Font('dim', 'style', 2)
    normal = Font('normal', 'style', 22)
    reset_all = Font('reset_all', 'style', 0)

    # ex_xx only support linux, mac

    ex_bold = Font('ex_bold', 'style')
    ex_dim = Font('ex_dim', 'style')
    ex_underlined = Font('ex_underlined', 'style')
    ex_blink = Font('ex_blink', 'style')
    ex_reverse = Font('ex_reverse', 'style')
    ex_hidden = Font('ex_hidden', 'style')
    ex_reset = Font('ex_reset', 'style')
    ex_res_bold = Font('ex_res_bold', 'style')
    ex_res_dim = Font('ex_res_dim', 'style')
    ex_res_underlined = Font('ex_res_underlined', 'style')
    ex_res_blink = Font('ex_res_blink', 'style')
    ex_res_reverse = Font('ex_res_reverse', 'style')
    ex_res_hidden = Font('ex_res_hidden', 'style')

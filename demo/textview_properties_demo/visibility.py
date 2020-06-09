# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'visibility = visible ', width=25, back=Back.green),
                           TextView('', ' hhhh ', visibility=Visibility.visible, back=Back.lightblack),
                           TextView('', ' end ', back=Back.red)],
                          [TextView('', 'visibility = invisible ', width=25, back=Back.green),
                           TextView('', ' hhhh ', visibility=Visibility.invisible, back=Back.lightblack),
                           TextView('', ' end ', back=Back.red)],
                          [TextView('', 'visibility = gone ', width=25, back=Back.green),
                           TextView('', ' hhhh ', visibility=Visibility.gone, back=Back.lightblack),
                           TextView('', ' end ', back=Back.red)],

                      ])

ctl.draw(auto_re_draw=False)
